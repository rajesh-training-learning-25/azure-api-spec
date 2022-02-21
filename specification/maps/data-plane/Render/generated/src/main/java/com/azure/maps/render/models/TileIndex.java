// Copyright (c) Microsoft Corporation. All rights reserved.
// Licensed under the MIT License.
// Code generated by Microsoft (R) AutoRest Code Generator.

package com.azure.maps.render.models;

import com.azure.core.annotation.Fluent;
import com.fasterxml.jackson.annotation.JsonProperty;

/** Parameter group. */
@Fluent
public final class TileIndex {
    /*
     * Zoom level for the desired tile.
     *
     * Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid)
     * for details.
     */
    @JsonProperty(value = "z", required = true)
    private int z;

    /*
     * X coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2<sup>`zoom`</sup> -1].
     *
     * Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid)
     * for details.
     */
    @JsonProperty(value = "x", required = true)
    private int x;

    /*
     * Y coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2<sup>`zoom`</sup> -1].
     *
     * Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid)
     * for details.
     */
    @JsonProperty(value = "y", required = true)
    private int y;

    /**
     * Get the z property: Zoom level for the desired tile.
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @return the z value.
     */
    public int getZ() {
        return this.z;
    }

    /**
     * Set the z property: Zoom level for the desired tile.
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @param z the z value to set.
     * @return the TileIndex object itself.
     */
    public TileIndex setZ(int z) {
        this.z = z;
        return this;
    }

    /**
     * Get the x property: X coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2&lt;sup&gt;`zoom`&lt;/sup&gt; -1].
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @return the x value.
     */
    public int getX() {
        return this.x;
    }

    /**
     * Set the x property: X coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2&lt;sup&gt;`zoom`&lt;/sup&gt; -1].
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @param x the x value to set.
     * @return the TileIndex object itself.
     */
    public TileIndex setX(int x) {
        this.x = x;
        return this;
    }

    /**
     * Get the y property: Y coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2&lt;sup&gt;`zoom`&lt;/sup&gt; -1].
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @return the y value.
     */
    public int getY() {
        return this.y;
    }

    /**
     * Set the y property: Y coordinate of the tile on zoom grid. Value must be in the range [0,
     * 2&lt;sup&gt;`zoom`&lt;/sup&gt; -1].
     *
     * <p>Please see [Zoom Levels and Tile
     * Grid](https://docs.microsoft.com/azure/location-based-services/zoom-levels-and-tile-grid) for details.
     *
     * @param y the y value to set.
     * @return the TileIndex object itself.
     */
    public TileIndex setY(int y) {
        this.y = y;
        return this;
    }
}
