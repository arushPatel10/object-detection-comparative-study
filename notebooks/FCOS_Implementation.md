# Fully Convolutional One-Stage Object Detection (FCOS)

## Overview
The Fully Convolutional One-Stage (FCOS) object detector is an anchor-free object detection model that treats object detection as a per-pixel prediction problem.

## Methodology
- **Base Network**: ResNet-50.
- **Anchor-Free Approach**: Divides the image into a grid and predicts the presence of objects at each grid point.
- **Key Components**: Class prediction, box regression, and centerness scores.

## Observations
- **Strengths**: Simplified training process, reduced computational overhead.
- **Weaknesses**: Moderate performance on small objects.

## Conclusion
FCOS simplifies the object detection process and performs well, though it may struggle with detecting smaller objects compared to other models.
