<template>
  <div class="list row">
    <div class="col-md-8">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="Search by title"
          v-model="title"/>
        <div class="input-group-append">
          <button class="btn btn-outline-secondary" type="button"
            @click="searchTitle"
          >
            Search
          </button>
        </div>
      </div>
    </div>
    <div class="col-md-6">
      <h4>Locations List</h4>
      <ul class="list-group">
        <li class="list-group-item"
          :class="{ active: index == currentIndex }"
          v-for="(location, index) in locations"
          :key="index"
          @click="setActiveLocation(location, index)"
        >
          {{ location.title }}
        </li>
      </ul>

      <button class="m-3 btn btn-sm btn-danger" @click="removeAllLocations">
        Remove All
      </button>
    </div>
    <div class="col-md-6">
      <div v-if="currentLocation">
        <h4>Location</h4>
        <div>
          <label><strong>Title:</strong></label> {{ currentLocation.title }}
        </div>
        <div>
          <label><strong>Description:</strong></label> {{ currentLocation.description }}
        </div>
        <div>
          <label><strong>Status:</strong></label> {{ currentLocation.published ? "Published" : "Pending" }}
        </div>

        <a class="badge badge-warning"
          :href="'/locations/' + currentLocation.id"
        >
          Edit
        </a>
      </div>
      <div v-else>
        <br />
        <p>Please click on a Location...</p>
      </div>
    </div>
  </div>
</template>

<script>
import LocationDataService from "../services/LocationDataService";

export default {
  name: "locations-list",
  data() {
    return {
      locations: [],
      currentLocation: null,
      currentIndex: -1,
      title: ""
    };
  },
  methods: {
    retrieveLocations() {
      LocationDataService.getAll()
        .then(response => {
          this.locations = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    refreshList() {
      this.retrieveLocations();
      this.currentLocation = null;
      this.currentIndex = -1;
    },

    setActiveLocation(location, index) {
      this.currentLocation = location;
      this.currentIndex = index;
    },

    removeAllLocations() {
      LocationDataService.deleteAll()
        .then(response => {
          console.log(response.data);
          this.refreshList();
        })
        .catch(e => {
          console.log(e);
        });
    },
    
    searchTitle() {
      LocationDataService.findByTitle(this.title)
        .then(response => {
          this.locations = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.retrieveLocations();
  }
};
</script>

<style>
.list {
  text-align: left;
  max-width: 750px;
  margin: auto;
}
</style>