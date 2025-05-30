import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";
import * as topojson from "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm";

export class BanMap {
    contentStrategy;
    renderStrategy;

    constructor(contentStrategy, renderStrategy) {
        this.contentStrategy = contentStrategy
        this.renderStrategy = renderStrategy
    }

    async createPlot() {
        const [states, bans] = await Promise.all([this.contentStrategy.loadMapData(), this.contentStrategy.loadBanData()])

        const plot = this.renderStrategy.createPlot(states, bans)
        return plot
    }
}

export class ContentStrategy {
    async loadMapData() {
        try {

            // const stateRes = await fetch('static/states-10m.json')
            const stateRes = await fetch(`${window.location.origin}/static/states-10m.json`);
            const us = await stateRes.json();
            const states = topojson.feature(us, us.objects.states)
            return states
        } catch (error) {
            console.log(error)
        }
    }

    async loadBanData() {
        //implement
    }
}

export class AllContent extends ContentStrategy {
    async loadBanData() {
        const banEndpoint = `${window.location.origin}/get-most-banned-states`;
        const banRes = await fetch(banEndpoint)
        const banList = await banRes.json();
        const banMap = new Map(banList.map(({ name, bans }) => [name, bans]))
        return banMap
    }
}

export class OneBookContent extends ContentStrategy {
    isbn; 
    constructor(isbn){
        super()
        this.isbn = isbn
    }

    async loadBanData() {
        const banEndpoint = `${window.location.origin}/get-most-banned-states-with-isbn?`;
        const banRes = await fetch(banEndpoint + new URLSearchParams({
            isbn: this.isbn,
        }))
        const banList = await banRes.json();
        const banMap = new Map(banList.map(({ name, bans }) => [name, bans]))
        return banMap
    }
}

class RenderStrategy {
    createPlot(states, banMap) {
        //impliment
    }
}

export class DetailedRender extends RenderStrategy {
    createPlot(states, banMap) {
        const withLegend = true;
        const withTooltip = true;

        const plot = Plot.plot({
            className: "map-plot",
            projection: "albers-usa",
            marks: [
                Plot.geo(
                    states,
                    {
                        stroke: "#f9f9f9",
                        strokeWidth: 0.4,
                        fill: (d) => banMap.get(d.properties.name),
                        title: (d) => `${d.properties.name} \n ${banMap.get(d.properties.name) ? banMap.get(d.properties.name) : 0} bans`,
                        tip: withTooltip,
                    }
                )],
            color: {
                range: ["#F9D6D6", "#F1AFAF", "#E98282", "#D14F4F", "#B22E2E"],
                unknown: "#464548",
                type: "log",
                label: withLegend ? "Number of book bans" : null,
                legend: withLegend,
            }

        })

        return plot
    }
}
export class SimpleRender extends RenderStrategy {
    createPlot(states, banMap) {
        const withLegend = false;
        const withTooltip = false;

        const plot = Plot.plot({
            className: "map-plot",
            projection: "albers-usa",
            marks: [
                Plot.geo(
                    states,
                    {
                        stroke: "#f9f9f9",
                        strokeWidth: 0.4,
                        fill: (d) => banMap.get(d.properties.name),
                        title: (d) => `${d.properties.name} \n ${banMap.get(d.properties.name) ? banMap.get(d.properties.name) : 0} bans`,
                        tip: withTooltip,
                    }
                )],
            color: {
                range: ["#F9D6D6", "#F1AFAF", "#E98282", "#D14F4F", "#B22E2E"],
                unknown: "#464548",
                type: "log",
                label: withLegend ? "Number of book bans" : null,
                legend: withLegend,
            }

        })
        console.log(plot)

        return plot
    }
}