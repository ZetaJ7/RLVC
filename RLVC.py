import os
import argparse

parser = argparse.ArgumentParser(
      formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--path", default='BasketballPass')
parser.add_argument("--output", default='')
parser.add_argument("--frame", type=int, default=100)
parser.add_argument("--f_P", type=int, default=6)
parser.add_argument("--b_P", type=int, default=6)
parser.add_argument("--mode", default='PSNR', choices=['PSNR', 'MS-SSIM'])
parser.add_argument("--metric", default='PSNR', choices=['PSNR', 'MS-SSIM'])
parser.add_argument("--python_path", default='python')
parser.add_argument("--CA_model_path", default='./CA_EntropyModel_Test/')
parser.add_argument("--l", type=int, default=1024, choices=[8, 16, 32, 64, 256, 512, 1024, 2048])
parser.add_argument("--entropy_coding", type=int, default=1)
parser.add_argument("--w", type=int, default=0)
parser.add_argument("--h", type=int, default=0)
parser.add_argument("--f_input", type=int, default=0)

args = parser.parse_args()

# os.system(args.python_path + ' Recurrent_AutoEncoder.py --frame ' + str(args.frame)
#           + ' --f_P ' + str(args.f_P) + ' --b_P ' + str(args.b_P) + ' --mode ' + args.mode + ' --metric ' + args.metric
#           + ' --python_path ' + args.python_path + ' --CA_model_path ' + args.CA_model_path
#           + ' --l ' + str(args.l) + )
#
# os.system(args.python_path + ' Recurrent_Prob_Model.py --frame ' + str(args.frame)
#           + ' --f_P ' + str(args.f_P) + ' --b_P ' + str(args.b_P) + ' --mode ' + args.mode
#           + ' --l ' + str(args.l) + ' --entropy_coding ' + str(args.entropy_coding))

os.system(args.python_path + ' Recurrent_AutoEncoder.py --frame ' + str(args.frame)
          + ' --f_P ' + str(args.f_P) + ' --b_P ' + str(args.b_P) + ' --mode ' + args.mode + ' --metric ' + args.metric
          + ' --python_path ' + args.python_path + ' --CA_model_path ' + args.CA_model_path + ' --path ' + str(args.path)
          + ' --l ' + str(args.l) + ' --output ' + str(args.output) + ' --w '+ str(args.w) + ' --h ' +str(args.h) + ' --f_input ' + str(args.f_input))

os.system(args.python_path + ' Recurrent_Prob_Model.py --frame ' + str(args.frame)
          + ' --f_P ' + str(args.f_P) + ' --b_P ' + str(args.b_P) + ' --mode ' + args.mode  + ' --path ' + str(args.path)
          + ' --l ' + str(args.l) + ' --entropy_coding ' + str(args.entropy_coding) + ' --output ' + str(args.output) + ' --w '+ str(args.w) + ' --h ' +str(args.h) + ' --f_input ' + str(args.f_input))

