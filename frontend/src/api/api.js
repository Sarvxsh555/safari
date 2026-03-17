import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000";

export const getOverview = () => axios.get(`${BASE_URL}/overview`);
export const getMapData = () => axios.get(`${BASE_URL}/map-data`);
export const getHotspots = () => axios.get(`${BASE_URL}/top-hotspots`);
export const getShapGlobal = () => axios.get(`${BASE_URL}/shap/global`);
export const getTrend = () => axios.get(`${BASE_URL}/trend`);
export const getTable = () => axios.get(`${BASE_URL}/table-data`);
