_base_ = [
    '../_base_/models/fcn_litehr18.py', '../_base_/datasets/hrf.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_cos_40k.py'
]

norm_cfg = dict(type='SyncBN', requires_grad=True)
model = dict(
    decode_head=dict(
        type='FCNHead',
        in_channels=40,
        in_index=0,
        channels=40,
        input_transform=None,
        kernel_size=1,
        num_convs=0,
        concat_input=False,
        dropout_ratio=-1,
        num_classes=2,
        norm_cfg=norm_cfg,
        align_corners=False,
        sampler=dict(type='MaxPoolingPixelSampler', ratio=0.25, p=1.7),
        loss_decode=dict(
            type='CrossEntropyLoss',
            use_sigmoid=False,
            loss_weight=1.0
        )
    ),
    # test_cfg=dict(mode='slide', crop_size=(256, 256), stride=(170, 170))
    test_cfg=dict(mode='slide', crop_size=(1024, 1024), stride=(680, 680))
)
evaluation = dict(
    metric='mDice'
)
