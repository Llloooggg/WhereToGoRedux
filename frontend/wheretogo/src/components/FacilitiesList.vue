<template>
    <div class="facilities_container">
        <div class="facilities_content">
            <h1>Facilities</h1>
            <ul class="facilities_list">
                <li v-for="facility in facilities" :key="facility.id">
                    <h2>{{ facility.name }}</h2>
                    <p>{{ facility.address }}</p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            facilities: ['']
        }
    },
    methods: {
        async getData() {
            try {
                const response = await this.axios.get('http://127.0.0.1:8000/api/facilities');
                this.facilities = response.data;
                console.log(this.facilities)
            } catch (error) {
                console.log(error);
            }
        },
    },
    created() {
        this.getData();
    }
}
</script>