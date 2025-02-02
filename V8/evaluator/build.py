import os

from evaluator.coco_evaluator import COCOAPIEvaluator
from evaluator.voc_evaluator import VOCAPIEvaluator
from evaluator.crowdhuman_evaluator import CrowdHumanEvaluator
from evaluator.customed_evaluator import CustomedEvaluator
from evaluator.platenumber_evaluator import PlateNumberEvaluator
from evaluator.character_evaluator import CharacterEvaluator



def build_evluator(args, data_cfg, transform, device):
    # Basic parameters
    data_dir = os.path.join(args.root, data_cfg['data_name'])

    # Evaluator
    ## VOC Evaluator
    if args.dataset == 'voc':
        evaluator = VOCAPIEvaluator(data_dir  = data_dir,
                                    device    = device,
                                    transform = transform
                                    )
    ## COCO Evaluator
    elif args.dataset == 'coco':
        evaluator = COCOAPIEvaluator(data_dir  = data_dir,
                                     device    = device,
                                     transform = transform
                                     )
    ## CrowdHuman Evaluator
    elif args.dataset == 'crowdhuman':
        evaluator = CrowdHumanEvaluator(data_dir  = data_dir,
                                        device    = device,
                                        image_set = 'val',
                                        transform = transform
                                        )
    ## Custom dataset Evaluator
    elif args.dataset == 'ourdataset':
        evaluator = CustomedEvaluator(data_dir  = data_dir,
                                        device    = device,
                                        image_set = 'val',
                                        transform = transform
                                        )
    ## Plate Number dataset Evaluator
    elif args.dataset == 'plate_number':
        evaluator = PlateNumberEvaluator(data_dir  = data_dir,
                                        device    = device,
                                        image_set = 'val',
                                        transform = transform
                                        )
        
    ## Character dataset Evaluator
    elif args.dataset == 'character':
        evaluator = CharacterEvaluator(data_dir  = data_dir,
                                        device    = device,
                                        image_set = 'val',
                                        transform = transform
                                        )

    return evaluator
