import sys
import json
import time
import datetime
import random
from pathlib import Path
from rest import McM
from rest.utils.shell import describe_platform

# Create cookie files in the current execution folder
mcm_cookie_path = Path().cwd() / Path(f"mcm-homepage-cookie")
pmp_cookie_path = Path().cwd() / Path(f"pmp-homepage-cookie")
print(f"Creating session cookies: McM ({str(mcm_cookie_path)}) - pMp ({str(pmp_cookie_path)})")

# Create a client session for querying McM.
mcm = McM(dev=False, cookie=mcm_cookie_path)

# Also for pMp.
pmp = McM(dev=False, cookie=pmp_cookie_path)
pmp.server = pmp.server.replace('mcm', 'pmp')
pmp.session.headers.update(
    {"User-Agent": f"PdmV HTTP Client (pMp) for Homepage update: {describe_platform()}"}
)

def get_list_of_campaigns():
    mc_aod_campaigns = mcm.get('campaigns', query='prepid=*UL*RECO*')
    mc_mini_campaigns = mcm.get('campaigns', query='prepid=*MiniAOD*')
    mc_nano_campaigns = mcm.get('campaigns', query='prepid=*NanoAOD*')
    print('%s AOD started campaigns' % (len(mc_aod_campaigns)))
    print('%s MiniAOD started campaigns' % (len(mc_mini_campaigns)))
    print('%s NanoAOD started campaigns' % (len(mc_nano_campaigns)))
    campaigns = []
    for campaign in mc_aod_campaigns + mc_mini_campaigns + mc_nano_campaigns:
        campaign_prepid = campaign['prepid']
        campaigns.append(campaign_prepid)

    rereco_campaigns = pmp._get('api/objects?r=rereco_campaigns')
    print('%s ReReco campaigns' % (len(rereco_campaigns)))
    campaigns.extend(rereco_campaigns)
    if '--debug' in sys.argv:
        random.shuffle(campaigns)
        campaigns = campaigns[:15]
        print('Picking %s random campaigns' % (len(campaigns)))

    return campaigns


def aggregate_data_points(data, timestamps):
    """
    Given list of event dictionaries (time, done, produced, invalid, expected)
    and timestamps aggregate everything into nice objects at given times
    """
    points = []
    for timestamp in timestamps:
        point = {'done': 0, 'produced': 0, 'expected': 0, 'invalid': 0, 'time': timestamp}
        for key in data:
            for details in reversed(data[key]):
                if details['time'] <= timestamp:
                    point['done'] += details['done']
                    point['invalid'] += details['invalid']
                    point['produced'] += details['produced']
                    point['expected'] += details['expected']
                    break

        point['events'] = point['invalid'] + point['produced'] + point['done']
        point['change'] = 0
        if len(points) > 0:
            last_point = points[-1]
            point['change'] = point['events'] - last_point['events']

        points.append(point)

    return points


def get_week_timestamps():
    # Last week, per 8 hour timestamp
    # Round down to 8 hours
    now = datetime.datetime.now()
    last_point = datetime.datetime(now.year, now.month, now.day)
    while last_point < now:
        last_point += datetime.timedelta(hours=8)

    timestamps = []
    for _ in range(0, 22):
        timestamps.append(datetime.datetime.timestamp(last_point))
        last_point -= datetime.timedelta(hours=8)

    timestamps.sort()
    return timestamps


def get_month_timestamps():
    # Last 30 days, per day timestamp
    now = datetime.datetime.now()
    last_point = datetime.datetime(now.year, now.month, now.day)
    last_point += datetime.timedelta(days=1)
    timestamps = []
    for _ in range(0, 31):
        timestamps.append(datetime.datetime.timestamp(last_point))
        last_point -= datetime.timedelta(days=1)

    timestamps.sort()
    return timestamps


def get_quarter_timestamps():
    # Last 12 weeks, per week timestamp
    now = datetime.date.today()
    now -= datetime.timedelta(days=now.weekday())
    now += datetime.timedelta(weeks=1)  # Next Monday
    now = datetime.datetime(now.year, now.month, now.day)
    timestamps = []
    for i in range(0, 13):
        timestamps.append(datetime.datetime.timestamp(now - datetime.timedelta(weeks=i)))

    timestamps.sort()
    return timestamps


def get_six_months_timestamps():
    # Last 24 weeks, per week timestamp
    now = datetime.date.today()
    now -= datetime.timedelta(days=now.weekday())
    now += datetime.timedelta(weeks=1)  # Next Monday
    now = datetime.datetime(now.year, now.month, now.day)
    timestamps = []
    for i in range(0, 25):
        timestamps.append(datetime.datetime.timestamp(now - datetime.timedelta(weeks=i)))

    timestamps.sort()
    return timestamps


def get_year_timestamps(year=None):
    def add_month(dt):
        return datetime.datetime(dt.year if dt.month <= 11 else dt.year + 1,
                                 (dt.month + 1) if dt.month <= 11 else 1,
                                 dt.day)

    def subtract_month(dt):
        return datetime.datetime(dt.year if dt.month > 1 else dt.year - 1,
                                 (dt.month - 1) if dt.month > 1 else 12,
                                 dt.day)

    if year is None:
        # Last 12 months, per month timestamp
        now = datetime.date.today()
        now = datetime.datetime(now.year, now.month, 1)  # Beginning of this month
    else:
        now = datetime.datetime(year, 12, 1)

    now = add_month(now)
    timestamps = []
    for i in range(0, 13):
        timestamps.append(datetime.datetime.timestamp(now))
        now = subtract_month(now)

    timestamps.sort()
    return timestamps


granularity = 1000
priority_blocks = {
    'block0': '130000,',
    'block1': '110000,130000',
    'block2': '90000,110000',
    'block3': '85000,90000',
    'block4': '80000,85000',
    'block5': '70000,80000',
    'block6': '63000,70000',
    'block7': ',63000',
}
campaigns = {}
campaign_list = get_list_of_campaigns()

fetch_start = time.time()
for i, campaign in enumerate(campaign_list):
    print('Getting %s from pMp, %s/%s' % (campaign, i + 1, len(campaign_list)))
    campaigns[campaign] = pmp._get('api/historical?r=%s&granularity=%s&aggregate=False' % (campaign, granularity))['results']['data']

fetch_end = time.time()
print('Got %s campaigns in %.2fs' % (len(campaigns), fetch_end - fetch_start))
all_timestamps = {}

all_timestamps['week'] = get_week_timestamps()
all_timestamps['30_days'] = get_month_timestamps()
all_timestamps['12_weeks'] = get_quarter_timestamps()
all_timestamps['24_weeks'] = get_six_months_timestamps()
all_timestamps['12_months'] = get_year_timestamps()
# Get previous 2 years and current year as "monthly"
now = datetime.datetime.now()
for year in range(now.year - 2, now.year + 1):
    all_timestamps[f'{year}_monthly'] = get_year_timestamps(year)

print('Timestamp keys: %s' % (', '.join(list(all_timestamps.keys()))))

# Create an output folder to store JSON files
output_folder = Path().cwd() / Path("output")
output_folder.mkdir(mode=0o700, exist_ok=True)
print("Folder to store results: ", output_folder)

for timestamp_name, timestamps in all_timestamps.items():
    # Split all campaigns into nice equal timestamps
    changes = {}
    used_pwgs = set()
    used_blocks = set()
    timestamps = [x * 1000 for x in timestamps]
    for campaign_name in campaigns:
        for pwg in campaigns[campaign_name]:
            for block_name in campaigns[campaign_name][pwg]:
                block = aggregate_data_points({campaign_name: campaigns[campaign_name][pwg][block_name]}, timestamps)
                block = [x['change'] for x in block]
                block = block[1:]
                block_sum = sum(block)
                if block_sum > 0:
                    if campaign_name not in changes:
                        changes[campaign_name] = {}

                    if pwg not in changes[campaign_name]:
                        changes[campaign_name][pwg] = {}

                    changes[campaign_name][pwg][block_name] = block
                    used_pwgs.add(pwg)
                    used_blocks.add(block_name)

    changes = {'timestamps': timestamps,
               'data': changes,
               'pwgs': sorted(list(used_pwgs)),
               'blocks': sorted(list(used_blocks))}

    # print(json.dumps(changes, indent=4))
    if len(changes) > 0:
        with open(file=output_folder / Path(f"{timestamp_name}.json"), mode="w") as f:
            json.dump(changes, f)
    else:
        print('No results?')
