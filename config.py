import argparse


def get_options(parser=argparse.ArgumentParser()):
    parser.add_argument('--workers', type=int, default=0, help='number of data loading workers, you had better put it '
                                                               '4 times of your gpu')
    parser.add_argument('--batch_size', type=int, default=64, help='input batch size, default=64')
    parser.add_argument('--scale', type=int, default=2, help='scale of image, default=4')
    parser.add_argument('--niter', type=int, default=10, help='number of epochs to train for, default=10')
    parser.add_argument('--lr_g', type=float, default=3e-5, help='select the learning rate, default=3e-5')
    parser.add_argument('--lr_d', type=float, default=3e-5, help='select the learning rate, default=3e-5')
    parser.add_argument('--lr_milestones', type=list, default=[100000, 180000, 240000, 280000], help='select the learning rate, default=3e-5')
    parser.add_argument('--lr_gamma', type=float, default=0.5, help='select the learning rate, default=3e-5')
    parser.add_argument('--cyc_weight', type=int, default=1, help='select the learning rate, default=3e-5')
    parser.add_argument('--idt_weight', type=int, default=2, help='select the learning rate, default=3e-5')
    parser.add_argument('--geo_weight', type=int, default=1, help='select the learning rate, default=3e-5')
    parser.add_argument('--d_sr_weight', type=float, default=0.1, help='select the learning rate, default=3e-5')
    parser.add_argument('--seed', type=int, default=118, help="random seed")
    opt = parser.parse_args()

    return opt