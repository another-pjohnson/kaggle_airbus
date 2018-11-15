from train import train

'''
ship_grad_ratio = 0.85
border_grad_ratio = 0.5
train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=1.0, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=30, MINIBATCH_SIZE=1000,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load=None,
      MODEL_NAME='resnet34_0', BETA=100., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=5, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=1.0, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=5, MINIBATCH_SIZE=1000,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load=None,
      MODEL_NAME='resnet34_2', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=5, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=1.0, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=5, MINIBATCH_SIZE=1000,
      SGDR_MIN_LEARNING_RATE=6.5e-6, SGDR_MAX_LEARNING_RATE=1e-4, PATIENCE=128, model_load=None,
      MODEL_NAME='resnet34_3', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=5, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=1.0, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=5, MINIBATCH_SIZE=1000,
      SGDR_MIN_LEARNING_RATE=6.5e-6, SGDR_MAX_LEARNING_RATE=1e-3, PATIENCE=128, model_load=None,
      MODEL_NAME='resnet34_4', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=1, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.8, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=7, MINIBATCH_SIZE=10000,
      SGDR_MIN_LEARNING_RATE=6.5e-6, SGDR_MAX_LEARNING_RATE=1e-4, PATIENCE=128, model_load='checkpoints/256_256_resnet34_3_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_continue', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=8, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=40, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.6, TARGET_SIZE=256, VALID_IMG_COUNT=32, NUM_EPOCHS=40, MINIBATCH_SIZE=1000,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=2e-5, PATIENCE=128, model_load='checkpoints/256_256_resnet34_3_continue_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_continue2', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=True)

ship_grad_ratio = 0.5
border_grad_ratio = 0.75

# rebalance beta due to loss_weights diluting bce because more background class is included
train(VIRTUAL_BATCH_SIZE=4, GPU_BATCH_SIZE=4, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.6, TARGET_SIZE=512, VALID_IMG_COUNT=32, NUM_EPOCHS=10, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=5e-7, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/256_256_resnet34_3_continue2_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_sr05_br75', BETA=3., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=4, GPU_BATCH_SIZE=4, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.5, TARGET_SIZE=512, VALID_IMG_COUNT=32, NUM_EPOCHS=310, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/256_256_resnet34_3_continue2_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_sr05_br75_2', BETA=3., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=4, GPU_BATCH_SIZE=1, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.8, TARGET_SIZE=768, VALID_IMG_COUNT=16, NUM_EPOCHS=70, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/512_512_resnet34_3_sr05_br75_2_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_sr05_br75_2_no_loss_weights', BETA=1., KAPPA=10., USE_LOSS_WEIGHTS=False)

ship_grad_ratio = 0.10
border_grad_ratio = 0.75

train(VIRTUAL_BATCH_SIZE=4, GPU_BATCH_SIZE=2, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.8, TARGET_SIZE=768, VALID_IMG_COUNT=16, NUM_EPOCHS=70, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/512_512_resnet34_3_sr05_br75_2_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_sr01_br75_2', BETA=3., KAPPA=1., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=4, GPU_BATCH_SIZE=2, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.8, TARGET_SIZE=768, VALID_IMG_COUNT=16, NUM_EPOCHS=70, MINIBATCH_SIZE=500,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/512_512_resnet34_3_sr05_br75_2_best_loss_weights.h5',
      MODEL_NAME='resnet34_3_sr01_br75_3', BETA=1., KAPPA=2., USE_LOSS_WEIGHTS=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=8, SGDR_CYCLE_LENGTH=100, SGDR_MULT_FACTOR=2.,
      SGDR_LR_DECAY=0.6, TARGET_SIZE=256, VALID_IMG_COUNT=64, NUM_EPOCHS=700, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=5e-7, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/256_256_resnet34_ohem_best_loss_weights.h5',
      MODEL_NAME='resnet34_ohem_dice', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=False, SHIP_GRAD_RATIO=0.5,
      BORDER_GRAD_RATIO=0.75, OHEM=True)

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=4, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2., AUGMENT_IMG=False,
      SGDR_LR_DECAY=0.6, TARGET_SIZE=512, VALID_IMG_COUNT=64, NUM_EPOCHS=70, MINIBATCH_SIZE=100,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/256_256_resnet34_ohem_dice_best_f2_weights.h5',
      MODEL_NAME='resnet34_ohem_dice', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=False, SHIP_GRAD_RATIO=0.5,
      BORDER_GRAD_RATIO=0.75, OHEM=True)
'''

train(VIRTUAL_BATCH_SIZE=16, GPU_BATCH_SIZE=2, SGDR_CYCLE_LENGTH=10, SGDR_MULT_FACTOR=2., AUGMENT_IMG=False,
      SGDR_LR_DECAY=0.6, TARGET_SIZE=768, VALID_IMG_COUNT=64, NUM_EPOCHS=70, MINIBATCH_SIZE=800,
      SGDR_MIN_LEARNING_RATE=1e-6, SGDR_MAX_LEARNING_RATE=1e-5, PATIENCE=128, model_load='checkpoints/512_512_resnet34_ohem_dice_best_f2_weights.h5',
      MODEL_NAME='resnet34_ohem_dice', BETA=10., KAPPA=1., USE_LOSS_WEIGHTS=False, SHIP_GRAD_RATIO=0.5,
      BORDER_GRAD_RATIO=0.75, OHEM=True)