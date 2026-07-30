# PyTorch
```python
import torch

z = torch.zeros(5, 3)
print(z)
print(z.dtype)
```
PyTorch formats all Tensors to allocate as torch.float32 in its standard practice.

```python
import torch

r1 = torch.ones(2, 3)
r2 = torch.ones(2, 3) * 2
r3 = r1 + r2
print(r3) # Every element should be 3 since the tensors are the same size (where in this case, tensors are the matrices)

r1 = torch.ones(2, 3)
r2 = torch.ones(3, 2)
r3 = r1 + r2 # This should fail because r1 and r2 are not the same size, and cannot be added together
```
Tensors can all complete Linear Algebra operations.

```python
# Automatic Differentiation Engine
x = torch.randn(1, 10)      #The Input
prev_h = torch.randn(1, 20) #Hidden state
W_h = torch.randn(20, 20)   #Learning weight for hidden state
W_x = torch.randn(20, 10)   #Learning weight for input

i2h = torch.mm(W_x, x.t()) #Multiply weights by their respective tensors
h2h = torch.mm(W_h, prev_h.t())
next_h = i2h + h2h         #Add outputs of two matrix multiplications
net_h = next_h.tanh()      #Pass result through tanh function

loss = next_h.sum()        #Loss from model
```
