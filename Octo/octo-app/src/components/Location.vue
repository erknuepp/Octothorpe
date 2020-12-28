<template>
  <div v-if="currentLocation" class="edit-form">
    <h4>Location</h4>
    <form>
      <div class="form-group">
        <label for="title">Title</label>
        <input type="text" class="form-control" id="title"
          v-model="currentLocation.title"
        />
      </div>
      <div class="form-group">
        <label for="description">Description</label>
        <input type="text" class="form-control" id="description"
          v-model="currentLocation.description"
        />
      </div>

      <div class="form-group">
        <label><strong>Status:</strong></label>
        {{ currentLocation.published ? "Published" : "Pending" }}
      </div>
    </form>

    <button class="badge badge-primary mr-2"
      v-if="currentLocation.published"
      @click="updatePublished(false)"
    >
      UnPublish
    </button>
    <button v-else class="badge badge-primary mr-2"
      @click="updatePublished(true)"
    >
      Publish
    </button>

    <button class="badge badge-danger mr-2"
      @click="deleteLocation"
    >
      Delete
    </button>

    <button type="submit" class="badge badge-success"
      @click="updateLocation"
    >
      Update
    </button>
    <p>{{ message }}</p>
  </div>

  <div v-else>
    <br />
    <p>Please click on a Location...</p>
  </div>
</template>

<script>
import LocationDataService from "../services/LocationDataService";

export default {
  name: "location",
  data() {
    return {
      currentLocation: null,
      message: ''
    };
  },
  methods: {
    getLocation(id) {
      LocationDataService.get(id)
        .then(response => {
          this.currentLocation = response.data;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updatePublished(status) {
      var data = {
        id: this.currentLocation.id,
        title: this.currentLocation.title,
        description: this.currentLocation.description,
        published: status
      };

      LocationDataService.update(this.currentLocation.id, data)
        .then(response => {
          this.currentLocation.published = status;
          console.log(response.data);
        })
        .catch(e => {
          console.log(e);
        });
    },

    updateLocation() {
      LocationDataService.update(this.currentLocation.id, this.currentLocation)
        .then(response => {
          console.log(response.data);
          this.message = 'The location was updated successfully!';
        })
        .catch(e => {
          console.log(e);
        });
    },

    deleteLocation() {
      LocationDataService.delete(this.currentLocation.id)
        .then(response => {
          console.log(response.data);
          this.$router.push({ name: "locations" });
        })
        .catch(e => {
          console.log(e);
        });
    }
  },
  mounted() {
    this.message = '';
    this.getLocation(this.$route.params.id);
  }
};
</script>

<style>
.edit-form {
  max-width: 300px;
  margin: auto;
}
</style>