# nebula
Blender tool to make gaussian splats with geometry nodes.

## Usage

First, go to the script workspace and hit play on the script. This script will set an empty's position/rotation to the viewport camera's to make the gaussian splats face it properly for preview.

Gaussians in Blender are simply point cloud data with custom attributes matching the 3DGS gaussian splat file ply format (without spherical harmonics for now).

To see them, put a "Render Gaussians" geometry node group as a modifier onto the object with the gaussians.

Other helpful node groups include:

1. Gaussian (just makes a gaussian manually)
2. Apply Gaussian Parameters (if you have existing points this is much more efficient)
3. Gaussian Line (give a start and end point, color and thickness, and it'll draw a nice gaussian for you)
4. Gaussian Polyline (Any mesh with edges will be turned into a gaussian line wireframe, with vertex colors for the gaussian colors.)
5. Gaussian Curve (Same as polyline but for curves. You may want to resample curves before doing this as it will be weird otherwise. Curve radius determines line thickness.)
6. Jitter (slightly moves gaussians randomly to produce a turbulent effect)
7. Gaussian Wiggle (moves gaussians over time)
8. Gaussian Heating (Adds emission to gaussians according to temperature, making them realistically heat up)

## Quirks

Because this is using geometry nodes, this is a system to billboard gaussians so Blender can render them as if they were mesh particles.

This means all processing for gaussians is done on CPU except for rendering them, despite being instanced. This is unavoidable as long as Geometry Nodes calculates on CPU.

Speaking of which... due to Blender's quirks (geonodes will run on hidden objects) you must enable "Disable in Viewport" in the outliner panel's filters and disable that for each object you do not want geonodes to process every frame!

It will process it every frame because the viewport script updates the empty object's transform every frame.
