> [!IMPORTANT]  
> This repository has been migrated to the PPD Technical Support team inside the CERN GitLab instance: [pdmv-homepage](https://gitlab.cern.ch/cms-ppd/technical-support/web-services/Homepage). Please open and follow issues directly there, do not open or follow them here!

# PdmV Homepage

Homepage of Physics Data And Monte Carlo Validation group in CMS experiment. Data is taken from pMp.

## Plot

Plot shows a summary of MiniAOD and NanoAOD campaigns of Monte Carlo and Data ReReco production over time. Campaigns in each bar are sorted in same order as in table below. Hovering mouse cursor over a histogram bar will highlight row of same campaign in the table below. Clicking on histogram bar will set campaign filter to that campaign only. Clicking on histogram bar if only one campaign is selected will switch to all campaigns being selected.

### Table

Table shows sum of events produced in MiniAOD and NanoAOD campaign of Monte Carlo and Data ReReco. Table is sorted in descending order based on total number of events produced in selected time range. Hovering mouse cursor over a table row will highlight same campaign in the plot. Clicking on table row will set campaign filter to that campaign only. Clicking on table row if only one campaign is selected will switch to all campaigns being selected.

### Options

#### Priority block filter

Priority block filter allows to filter statistics by their priority in computing.
 * Block 0 - ⩾ 130000
 * Block 1 - 110000 - 129999
 * Block 2 - 90000 - 109999
 * Block 3 - 85000 - 89999
 * Block 4 - 80000 - 84999
 * Block 5 - 70000 - 79999
 * Block 6 - 63000 - 69999
 * Block 7 - ⩽ 62999

#### Campaign filter

Campaign filter allows to show or hide certain campaigns. Initially only MiniAOD campaigns are selected and NanoAOD campaigns are unselected. Invert All button switches states of all checkboxes, that is all checked become unchecked and vice versa. Reset button resets checkboxes to initial state where only MiniAOD campaigns are selected.

#### PWG filter

PWG filter allows to filter statistics by PWG. ReReco requests have a special PWG - ReReco.

#### Plot mode

Plot mode allows to select how events are counted in each histogram bar:
  * Cumulative - adds events from bar to the left (0 for leftmost bar) to events that were produced in time period indicated in X axis
  * Newly produced - shows how many events were produced in time period indicated in X axis

#### Plot scale

Plot scale allows to choose Y axis scale - Linear or Logarithmic.

#### Bubble legend

Bubble legend is a legend to the right of the histogram that shows campaign name for each color in the histogram. Legend is sorted in descending order based on total number of events produced in selected time range. Legend is limited to 18 items.

#### Time range

Time range allows to chose time range to be shown in the plot:
 * 7 days - last 7 days, one bar representing 8 hours
 * 30 days - last 30 days, one bar representing 1 day
 * 12 weeks - last 12 weeks, one bar representing 1 week
 * 12 months - last 12 months, one bar representing 1 month
 * 2019 monthly - 12 months of 2019, one bar representing 1 month

When time range is selected, priority, campaign and PWG filters are reset.

## Organigram

Organigram shows current structure of PdmV group.

## Important Links

List of links to PdmV tools, HyperNews and knowledge bases.
