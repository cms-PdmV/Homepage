<template>
  <div>
    <v-expansion-panels>
      <v-expansion-panel>
        <v-expansion-panel-header>Priority Block Filter&nbsp;
          <span class="selected-number-text" v-if="dataFiltersNumbers.blocks.selected != dataFiltersNumbers.blocks.all">
            <i>
              (selected {{dataFiltersNumbers.blocks.selected}} out of {{dataFiltersNumbers.blocks.all}})
            </i>
          </span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-checkbox
            class="nomargin"
            v-for="block in dataFilters.blocks"
            v-model="block.selected"
            :key="block.title"
            :label="block.displayName"
          ></v-checkbox>
          <v-btn small @click="setAll(dataFilters.blocks, true)" class="mr-2 mt-2 primary">Select all</v-btn>
          <v-btn small @click="setAll(dataFilters.blocks, false)" class="mt-2 primary">Deselect all</v-btn>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Campaign Filter&nbsp;
          <span class="selected-number-text" v-if="dataFiltersNumbers.campaigns.selected != dataFiltersNumbers.campaigns.all">
            <i>
              (selected {{dataFiltersNumbers.campaigns.selected}} out of {{dataFiltersNumbers.campaigns.all}})
            </i>
          </span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-checkbox
            class="nomargin"
            v-for="campaign in dataFilters.campaigns"
            v-model="campaign.selected"
            :key="campaign.name"
            :label="campaign.name"
          ></v-checkbox>
          <v-btn small @click="setAll(dataFilters.campaigns, true)" class="mr-2 mt-2 primary">Select all</v-btn>
          <v-btn small @click="setAll(dataFilters.campaigns, false)" class="mr-2 mt-2 primary">Deselect all</v-btn>
          <v-btn small @click="invert(dataFilters.campaigns)" class="mr-2 mt-2 primary">Invert all</v-btn>
          <v-btn small @click="resetCampaigns(dataFilters.campaigns)" class="primary">Reset</v-btn>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>PWG Filter&nbsp;
          <span class="selected-number-text" v-if="dataFiltersNumbers.pwgs.selected != dataFiltersNumbers.pwgs.all">
            <i>
              (selected {{dataFiltersNumbers.pwgs.selected}} out of {{dataFiltersNumbers.pwgs.all}})
            </i>
          </span>
        </v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-row style="margin-top: 0; margin-bottom: 0">
            <v-col v-for="pwg in dataFilters.pwgs"
                   cols="6"
                   sm="4"
                   class="pt-0 pb-0"
                   :key="pwg.name">
              <v-checkbox
                class="nomargin"
                v-model="pwg.selected"
                :label="pwg.name"
              ></v-checkbox>
            </v-col>
          </v-row>
          <v-btn small @click="setAll(dataFilters.pwgs, true)" class="mr-2 mt-2 primary">Select all</v-btn>
          <v-btn small @click="setAll(dataFilters.pwgs, false)" class="mt-2 primary">Deselect all</v-btn>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Plot Mode</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-radio-group v-model="plotMode" class="nomargin">
            <span title="Bars represent how many events in total were producted up to the end of that time slot">
              <v-radio :key="'cumulative'" :label="'Cumulative'" :value="'cumulative'"></v-radio>
            </span>
            <span title="Bars represent how many events were produced in that time slot">
              <v-radio :key="'change'" :label="'Newly produced'" :value="'change'"></v-radio>
            </span>
          </v-radio-group>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Plot Scale</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-radio-group v-model="plotScale" class="nomargin">
            <span title="Make event axis linear">
              <v-radio :key="'linear'" :label="'Linear'" :value="'linear'"></v-radio>
            </span>
            <span title="Make event axis logarithmic">
              <v-radio :key="'log'" :label="'Logarithmic'" :value="'log'"></v-radio>
            </span>
          </v-radio-group>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Bubble Legend</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-radio-group v-model="bubbleLegend" class="nomargin">
            <span title="Hide color legend next to the plot">
              <v-radio :key="'off'" :label="'Hidden'" :value="'off'"></v-radio>
            </span>
            <span title="Show color legent next to the plot">
              <v-radio :key="'on'" :label="'Visible'" :value="'on'"></v-radio>
            </span>
          </v-radio-group>
        </v-expansion-panel-content>
      </v-expansion-panel>

      <v-expansion-panel>
        <v-expansion-panel-header>Time Range</v-expansion-panel-header>
        <v-expansion-panel-content>
          <v-radio-group v-model="timeRange" class="nomargin">
            <span title="Show last 7 days in 8 hour intervals">
              <v-radio :key="'week'" :label="'7 days'" :value="'week'"></v-radio>
            </span>
            <span title="Show last 30 days in 1 day intervals">
              <v-radio :key="'30_days'" :label="'30 days'" :value="'30_days'"></v-radio>
            </span>
            <span title="Show last 12 weeks in 1 week intervals">
              <v-radio :key="'12_weeks'" :label="'12 weeks'" :value="'12_weeks'"></v-radio>
            </span>
            <span title="Show last 24 weeks in 1 week intervals">
              <v-radio :key="'24_weeks'" :label="'24 weeks'" :value="'24_weeks'"></v-radio>
            </span>
            <span title="Show last 12 months in 1 month intervals">
              <v-radio :key="'12_months'" :label="'12 months'" :value="'12_months'"></v-radio>
            </span>
            <span v-for="year in years" :key="year + '_monthly'" :title="'Show ' + year + ' in 1 month intervals'">
              <v-radio :key="year + '_monthly'" :label="year + ' monthly'" :value="year + '_monthly'"></v-radio>
            </span>
          </v-radio-group>
          <small style="opacity: 0.4">Changing time range will reset priority, campaign and PWG filters</small>
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
  </div>
</template>

<script>

import Vue from 'vue'

export default {
  name: 'PdmVPlotFilter',
  data () {
    return {
      dataFilters: {
        blocks: [],
        campaigns: [],
        pwgs: [],
      },
      dataFiltersNumbers:{
        blocks: {
          all: 0,
          selected: 0
        },
        campaigns: {
          all: 0,
          selected: 0
        },
        pwgs: {
          all: 0,
          selected: 0
        },
      },
      plotMode: 'cumulative',
      plotScale: 'linear',
      bubbleLegend: 'off',
      timeRange: undefined,
      initialCampaigns: [],
      initialBlocks: [],
      initialPWGs: [],
      initializedFilters: false,
      previouslyShownCampaigns: [],
      years: [],
    }
  },
  created () {
    const query = this.$route.query;
    if (query.campaigns) {
        this.initialCampaigns = query.campaigns.split(',').filter(Boolean);
    }
    if (query.pwgs) {
        this.initialPWGs = query.pwgs.split(',').filter(Boolean);
    }
    if (query.blocks) {
        this.initialBlocks = query.blocks.split(',').filter(Boolean);
    }
    if (query.plot_mode) {
      this.plotMode = query.plot_mode;
    }
    if (query.plot_scale) {
      this.plotScale = query.plot_scale;
    }
    if (query.bubble_legend) {
      this.bubbleLegend = query.bubble_legend;
    }
    if (query.time_range) {
      this.timeRange = query.time_range;
    } else {
      this.timeRange = 'week';
    }
    const currentYear = new Date().getFullYear();
    this.years = [currentYear - 2, currentYear - 1, currentYear];
  },
  props: {
    fetchedData: {
      type: Object,
      default: () => {}
    },
    eventBus: {
      type: Object,
      default: () => undefined
    }
  },
  mounted () {
    const component = this;
    this.eventBus.$on('campaignClick', function (campaign) {
      let onlyCurrentSelected = component.dataFilters.campaigns.reduce(function(res, c) {return res && ((c.name === campaign.name) == (c.selected))}, true);
      if (onlyCurrentSelected && component.previouslyShownCampaigns.length) {
        component.dataFilters.campaigns.map(function(c) {c.selected = component.previouslyShownCampaigns.indexOf(c.name) !== -1});
        component.previouslyShownCampaigns = [];
      } else {
        component.previouslyShownCampaigns = component.dataFilters.campaigns.reduce(function(res, c) { if (c.selected) { res.push(c.name) } return res;}, []);
        component.dataFilters.campaigns.map(function(c) {c.selected = (c.name === campaign.name) || onlyCurrentSelected});
      }
    })
  },
  watch: {
    fetchedData () {
      this.prepareFilters()
    },
    dataFilters: {
      handler: function (newVal, oldVal) {
        if (this.initializedFilters) {
          // Delete query
          this.$router.replace({query: {}}).catch(() => {});
        }
        this.initializedFilters = true;
        let enabledBlocks = Object.keys(newVal.blocks).reduce(function(map, key) {
          if (newVal.blocks[key].selected) {
            map.push(newVal.blocks[key].name)
          }
          return map
        }, [])
        let enabledCampaigns = Object.keys(newVal.campaigns).reduce(function(map, key) {
          if (newVal.campaigns[key].selected) {
            map.push(newVal.campaigns[key].name)
          }
          return map
        }, [])
        let enabledPwgs = Object.keys(newVal.pwgs).reduce(function(map, key) {
          if (newVal.pwgs[key].selected) {
            map.push(newVal.pwgs[key].name)
          }
          return map
        }, [])

        this.dataFiltersNumbers.campaigns.all = newVal.campaigns.length;
        this.dataFiltersNumbers.blocks.all = newVal.blocks.length;
        this.dataFiltersNumbers.pwgs.all = newVal.pwgs.length;
        this.dataFiltersNumbers.campaigns.selected = enabledCampaigns.length;
        this.dataFiltersNumbers.blocks.selected = enabledBlocks.length;
        this.dataFiltersNumbers.pwgs.selected = enabledPwgs.length;

        this.eventBus.$emit('filterChange', {'campaigns': enabledCampaigns,
                                             'blocks': enabledBlocks,
                                             'pwgs': enabledPwgs})
      },
      deep: true
    },
    plotMode () {
      this.eventBus.$emit('plotModeChange', this.plotMode)
    },
    plotScale () {
      this.eventBus.$emit('plotScaleChange', this.plotScale)
    },
    bubbleLegend () {
      this.eventBus.$emit('bubbleLegendChange', this.bubbleLegend)
    },
    timeRange () {
      this.eventBus.$emit('timeRangeChange', this.timeRange)
    },
  },
  methods: {
    prepareFilters() {
      const component = this;
      let newFilters = {}
      newFilters.blocks = []
      newFilters.campaigns = []
      newFilters.pwgs = []
      if (this.fetchedData) {
        for (let campaignName in this.fetchedData.data) {
          newFilters.campaigns.push({'name': campaignName, 'selected': campaignName.toLowerCase().indexOf('nano') === -1});
        }
        newFilters.campaigns = newFilters.campaigns.sort(this.compareCampaigns)
        let availableBlocks = [{'name': 'block0', 'number': '0', 'displayName': 'Block 0 (130k)', 'selected': true, 'title': 'Priority ⩾ 130000'},
                               {'name': 'block1', 'number': '1', 'displayName': 'Block 1 (110k)', 'selected': true, 'title': 'Priority 110000 - 130000'},
                               {'name': 'block2', 'number': '2', 'displayName': 'Block 2 (90k)','selected': true, 'title': 'Priority 90000 - 109999'},
                               {'name': 'block3', 'number': '3', 'displayName': 'Block 3 (85k)','selected': true, 'title': 'Priority 85000 - 89999'},
                               {'name': 'block4', 'number': '4', 'displayName': 'Block 4 (80k)','selected': true, 'title': 'Priority 80000 - 84999'},
                               {'name': 'block5', 'number': '5', 'displayName': 'Block 5 (70k)','selected': true, 'title': 'Priority 70000 - 79999'},
                               {'name': 'block6', 'number': '6', 'displayName': 'Block 6 (63k)','selected': true, 'title': 'Priority 63000 - 69999'},
                               {'name': 'block7', 'number': '7', 'displayName': 'Block 7 (<63k)', 'selected': true, 'title': 'Priority ⩽ 63000'},];
        for (let availableBlock of availableBlocks) {
          if (this.fetchedData.blocks.includes(availableBlock.name)) {
            newFilters.blocks.push(availableBlock);
          }
        }
        for (let pwg of this.fetchedData.pwgs) {
          newFilters.pwgs.push({'name': pwg, 'selected': true});
        }
        if (this.initialCampaigns.length) {
          newFilters.campaigns.map(function(c) {c.selected = component.initialCampaigns.includes(c.name)});
          this.initialCampaigns = [];
        }
        if (this.initialPWGs.length) {
          newFilters.pwgs.map(function(p) {p.selected = component.initialPWGs.includes(p.name)});
          this.initialPWGs = [];
        }
        if (this.initialBlocks.length) {
          newFilters.blocks.map(function(b) {b.selected = component.initialBlocks.includes(b.number)});
          this.initialBlocks = [];
        }
      }
      this.dataFilters = newFilters;
    },
    setAll(objects, value) {
      for (let key of Object.keys(objects)) {
        objects[key].selected = value;
      }
    },
    invert(objects) {
      for (let key of Object.keys(objects)) {
        objects[key].selected = !objects[key].selected;
      }
    },
    resetCampaigns(objects) {
      for (let key of Object.keys(objects)) {
        objects[key].selected = objects[key].name.toLowerCase().indexOf('nano') === -1;
      }
    },
    compareCampaigns(a, b) {
      let aName = a.name.toLowerCase();
      let bName = b.name.toLowerCase();
      let aNano = aName.indexOf('nano') !== -1;
      let bNano = bName.indexOf('nano') !== -1;
      if (!aNano && bNano) {
        return -1;
      }
      if (aNano && !bNano) {
        return 1;
      }
      if (aName < bName) {
        return -1;
      }
      if  (aName > bName) {
        return 1;
      }
      return 0;
    },
    getAllValues() {
      return {'campaigns': this.dataFilters.campaigns,
              'blocks': this.dataFilters.blocks,
              'pwgs': this.dataFilters.pwgs,
              'plotMode': this.plotMode,
              'plotScale': this.plotScale,
              'bubbleLegend': this.bubbleLegend,
              'timeRange': this.timeRange,}
    }
  }
}

</script>

<style>
.nomargin {
  margin: 0 !important;
  padding: 0 !important;
}

.v-input--radio-group__input > span {
  padding-bottom: 8px;
}

.v-input__slot {
  margin-bottom: 0 !important;
}

.selected-number-text {
  opacity: 0.6;
  margin-left: 4px;
}

</style>
