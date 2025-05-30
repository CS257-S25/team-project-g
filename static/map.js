/**
 * Module for creating map plots
 */

import * as Plot from "https://cdn.jsdelivr.net/npm/@observablehq/plot@0.6/+esm";
import * as topojson from "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm";

export class BanMap {
  /**
   * Class for creating map plots of banned books
  */
  contentStrategy;
  renderStrategy;

  constructor(contentStrategy, renderStrategy) {
    /**
     * Constructor for the BanMap class
     * @param {ContentStrategy} contentStrategy - strategy for which content to display
     * @param {RenderStrategy} renderStrategy - strategy for how to render the map
     */
    this.contentStrategy = contentStrategy
    this.renderStrategy = renderStrategy
  }

  async createPlot() {
    /**
     * Method for creating a map plot
     * @returns - the map plot html element
    */
    const [states, bans] = await Promise.all([this.contentStrategy.loadMapData(), this.contentStrategy.loadBanData()])

    const plot = this.renderStrategy.createPlot(states, bans)
    return plot
  }
}

export class ContentStrategy {
  /**
   * Class for loading the content to display
   */
  async loadMapData() {
    /**
     * Method for loading map data of states
     * @returns - state topology
     */
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
    /**
     * Method for loading ban data to be implimented
     * @returns - a map of states to number of bans
     */
  }
}

export class AllContent extends ContentStrategy {
  /**
   * Class for loading the content to display for all bans
   */
  async loadBanData() {
    /**
     * Method for loading all ban data
     * @returns - a map of states to number of bans
     */
    const banEndpoint = `${window.location.origin}/get-most-banned-states`;
    const banRes = await fetch(banEndpoint)
    const banList = await banRes.json();
    const banMap = new Map(banList.map(({ name, bans }) => [name, bans]))
    return banMap
  }
}

export class OneBookContent extends ContentStrategy {
  /**
   * Class for loading the content to display for bans of one book
   */
  isbn;

  constructor(isbn) {
    /**
     * Constructor for the OneBookContent ContentStrategy
     * @param {String} isbn - isbn of book
     */
    super()
    this.isbn = isbn
  }

  async loadBanData() {
    /**
     * Method for loading ban data for one book
     * @returns - a map of states to number of bans
     */
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
  /**
   * Class for creating a plot based on ban data
   */
  createPlot(states, banMap) {
    /**
     * Method for creating a plot to be implimented
     * @param states - state topology
     * @param banMap - map of states to bans
     * @return - map plot
     */
  }
}

export class DetailedRender extends RenderStrategy {
  /**
   * Class for creating a plot based on ban data with legend and tooltip
   */
  createPlot(states, banMap) {
    /**
     * Method for creating a plot
     * @param states - state topology
     * @param banMap - map of states to bans
     * @return - map plot
     */
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
            tip: true,
          }
        )],
      color: {
        range: ["#F9D6D6", "#F1AFAF", "#E98282", "#D14F4F", "#B22E2E"],
        unknown: "#464548",
        type: "log",
        label: "Number of book bans",
        legend: true,
      }

    })

    return plot
  }
}
export class SimpleRender extends RenderStrategy {
  /**
   * Class for creating a plot based on ban data with no extra information
   */
  createPlot(states, banMap) {
    /**
     * Method for creating a plot
     * @param states - state topology
     * @param banMap - map of states to bans
     * @return - map plot
     */
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
