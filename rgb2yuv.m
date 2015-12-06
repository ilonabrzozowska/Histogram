function ret = rgb2yuv(x)

R = x(:,:,1);
G = x(:,:,2);
B = x(:,:,3);

Y  =  0.229*R + 0.587*G + 0.114*B;
Cb = -0.168*R - 0.331*G - 0.500*B;
Cr =  0.500*R - 0.418*G + 0.082*B;

ret = Y;
ret(:,:,2) = Cb;
ret(:,:,3) = Cr;

