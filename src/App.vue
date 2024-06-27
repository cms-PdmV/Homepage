<template>
  <v-app>
    <v-app-bar app style="background-color: #fff">
      <a href="" class="no-decoration">
        <v-toolbar-title class="headline">
          <span>PdmV</span>
          <span class="font-weight-light">Homepage</span>
        </v-toolbar-title>
      </a>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://cms-pdmv-prod.web.cern.ch/mcm"
        target="_blank"
        class="d-none d-md-flex"
      >
        <span class="mr-2">McM</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      <v-btn
        text
        href="https://cms-pdmv-prod.web.cern.ch/pmp"
        target="_blank"
        class="d-none d-md-flex"
      >
        <span class="mr-2">pMp</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      <v-btn
        text
        href="https://hypernews.cern.ch/HyperNews/CMS/get/prep-ops.html"
        target="_blank"
        class="d-none d-md-flex"
      >
        <span class="mr-2">HyperNews</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      <v-btn
        text
        href="https://cms-pdmv-prod.web.cern.ch/valdb"
        target="_blank"
        class="d-none d-md-flex"
      >
        <span class="mr-2">ValDB</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
      <v-btn
        text
        href="https://cms-pdmv-prod.web.cern.ch/relmon"
        target="_blank"
        class="d-none d-md-flex"
      >
        <span class="mr-2">RelMon</span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<style scoped>

.headline {
  color: rgba(0, 0, 0, 0.87) !important;
}

a.no-decoration {
  text-decoration: none;
}

</style>
