# CenterNet

## Overview
CenterNet is an object detection model that builds upon the CornerNet detector. CenterNet uses keypoint triplets (two corners and the center) to define a bounding box and improves accuracy by checking the patterns within the central region.

## Methodology
- **Base Network**: Hourglass-104.
- **Key Components**: Center Pooling, Cascade Corner Pooling to extract features from the center and corners.
- **Bounding Box Predictions**: Analyzes the central region to ensure accuracy.

## Observations
- **Strengths**: Accurate localization of objects.
- **Weaknesses**: Slower inference time compared to other models.

## Conclusion
CenterNet performs well in terms of accuracy but may not be suitable for real-time applications due to its slower speed.
