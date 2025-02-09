import torch
from torch import nn
import torch.nn.functional as F
from torch.autograd import Variable


# 加注释
class LeNet(nn.Module):
    def __init__(self):
        # nn.Module的子类函数必须在构造函数中执行父类的构造函数
        super(LeNet, self).__init__()  # 等价与nn.Module.__init__()

        # nn.Conv2d返回的是一个Conv2d class的一个对象，该类中包含forward函数的实现
        # 当调用self.conv1(input)的时候，就会调用该类的forward函数
        self.conv1 = nn.Conv2d(1, 6, (5, 5))  # output (N, C_{out}, H_{out}, W_{out})`
        self.conv2 = nn.Conv2d(6, 16, (5, 5))
        self.fc1 = nn.Linear(256, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        # F.max_pool2d的返回值是一个Variable， input:(10,1,28,28)  ouput:(10, 6, 12, 12)
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        # input:(10, 6, 12, 12)   output:(10,6,4,4)
        x = F.max_pool2d(F.relu(self.conv2(x)), (2, 2))
        # 固定样本个数，将其他维度的数据平铺，无论你是几通道，最终都会变成参数， output:(10, 256)
        x = x.view(x.size()[0], -1)
        # 全连接
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))

        # 返回值也是一个Variable对象
        return x


def output_name_and_params(net):
    for name, parameters in net.named_parameters():
        print('name: {}, param: {}'.format(name, parameters))


if __name__ == '__main__':
    net = LeNet()
    print('net: {}'.format(net))
    params = net.parameters()  # generator object
    print('params: {}'.format(params))
    output_name_and_params(net)

    input_image = torch.FloatTensor(10, 1, 28, 28)

    # 和tensorflow不一样，pytorch中模型的输入是一个Variable，而且是Variable在图中流动，不是Tensor。
    # 这可以从forward中每一步的执行结果可以看出
    input_image = Variable(input_image)

    output = net(input_image)
    print('output: {}'.format(output))
    print('output.size: {}'.format(output.size()))
