# Montein Dynmap Markers

List of Dynmap markers for the Montein Minecraft Server.

## Format

### Set

- `id`: The ID of the set
- `label`: The label of the set
- `showlabel`: Whether labels for markers in this set are permanently visible
- `prio`: The set priority
- `hide`: Whether the set is enabled by default
- `minzoom`: The minimum zoom markers in the set render at
- `maxzoom`: The maximum zoom markers in the set render at
- `deficon`: The default icon of markers in the set
- `enabled`: Whether the set should be added

### Area

- `id`: The ID of the area marker
- `label`: The label of the area marker
- `description`: The text shown in the popup
- `markup`: Whether the description can contain HTML markup
- `linecolor`: The color of the outline
- `lineweight`: The thickness of the outline
- `lineopacity`: The opacity of the outline
- `fillcolor`: The color of the fill
- `fillopacity`: The opacity of the fill
- `showgreeting`: Whether a greeting should be shown when the player enters the area
- `minzoom`: The minimum zoom the area marker will render at
- `maxzoom`: The maximum zoom the area marker will render at
- `world`: The world the area marker is in
- `points`: Array of x, y coordinates of the corners
- `enabled`: Whether the area marker should be added

### Marker

- `id`: The ID of the marker
- `label`: The label of the marker
- `description`: The text shown in the popup
- `markup`: Whether the description can contain HTML markup
- `icon`: The icon of the marker
- `minzoom`: The minimum zoom the marker will render at
- `maxzoom`: The maximum zoom the marker will render at
- `world`: The world the marker is in
- `x`, `y`, `z`: The coordinates of the marker
- `enabled`: Whether the marker should be added

## Icons

| Icon | Name |
|:-----|:-----|
| ![Fuel Icon](icons/md-fuel.png) | md-fuel |
| ![Police Icon](icons/md-police.png) | md-police |