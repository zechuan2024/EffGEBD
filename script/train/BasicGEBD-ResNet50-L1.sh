# ******************training BasicGEBD-ResNet50-L1*************************
python train.py \
--expname x1_r50_basic \
MODEL.BACKBONE.NAME 'resnet50' \
MODEL.CAT_PREV False \
MODEL.FPN_START_IDX 0 \
MODEL.HEAD_CHOICE [0] \
SOLVER.BATCH_SIZE 1 \
MODEL.IS_BASIC True
#**************************************************************************