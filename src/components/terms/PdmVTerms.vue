<template>
  <div style="background: white;" class="pa-2 elevation-3">
    <h1 class="ml-2">Important Links</h1>
    <ul>
      <li>Monte Carlo
        <ul>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/mcm/'">McM</a> - Monte Carlo management website. Main tool for creating, joining and submitting MC requests</li>
          <li><a target="_blank" :href="'https://cms-pdmv.gitbook.io/project/'">Monte Carlo knowledge base</a> - useful technical information for MC contacts and MC requests managers working in PdmV
            <ul>
              <li><a target="_blank" :href="'https://cms-pdmv.gitbook.io/project/mccontact'">MC contact's corner</a> - useful information for Monte Carlo contacts about how to act in McM</li>
              <li><a target="_blank" :href="'https://cms-pdmv.gitbook.io/project/analyzers-corner'">MC analyzer's corner</a> - basic explanation of the glossary, needed for analysers to understand the logic of the central MC production</li>
            </ul>
          </li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/grasp/'">GrASP</a> - Group Analysis Sample Page</li>
          <li><a target="_blank" :href="'https://twiki.cern.ch/twiki/bin/view/CMS/PdmVMcCampaigns  '">Campaigns TWiki</a> - Monte Carlo campaigns TWiki</li>        
          <li><a target="_blank" :href="'https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun2LegacyAnalysis'">Analysis table</a> - analysis guideline</li>
          <li><a target="_blank" :href="'https://hypernews.cern.ch/HyperNews/CMS/get/prep-ops.html'">MC HyperNews</a> - forum dedicated to the discussion and advertisement of requests managed within the McM</li>
        </ul>
      </li>
      <li>Data ReReco
        <ul>
          <li><a target="_blank" :href="'https://twiki.cern.ch/twiki/bin/view/CMS/PdmVDataReprocessing'">Reprocessing TWiki</a> - information about data reprocessing in PdmV</li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/rereco/'">ReReco</a> - ReReco management website</li>
          <li><a target="_blank" :href="'https://cms-pdmv.gitbook.io/data-rereco/'">ReReco documentation</a> - ReReco tool documentation</li>
        </ul>
      </li>
      <li>Release Validation
        <ul>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/relmon/'">RelMon</a> - RelMon reports</li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/valdb/'">ValDB</a> - Validation reports</li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/relval/'">RelVal</a> - RelVal management website</li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/relmonservice/'">RelMonService</a> - RelMon Service</li>
          <li><a target="_blank" :href="'https://cms-pdmv.gitbook.io/release-validation/'">Release validation docs</a> - RelVal and RelMonService tool documentation</li>
        </ul>
      </li>
      <li>Misc
        <ul>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/pmp/'">pMp</a> - Production monitoring website</li>
          <li><a target="_blank" :href="'https://cms-pdmv-prod.web.cern.ch/stats/'">Stats</a> - PdmV cache of ReqMgr2 and DBS</li>
          <li><a target="_blank" :href="'https://twiki.cern.ch/twiki/bin/view/CMS/PdmV'">TWiki</a> - PdmV TWiki</li>
          <li><a target="_blank" :href="'https://pdmv-pages.web.cern.ch/'">PdmV pages</a> - various small PdmV pages</li>
        </ul>
      </li>
    </ul>
  </div>
</template>

<script type="text/javascript">

  export default {
    name: 'PdmVTerms',
    // svg cannot be property by itself, changes object type during assignment, within ddd object is fine
    data () {
      return {

      }
    },

    props: {

    },

    watch: {

    },
    methods: {

    },
    mounted () {

    }
  };

</script>

<style scoped>

</style>
