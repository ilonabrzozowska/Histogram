function [] = present(path)

I = imread(path)
size(I)
origin = histeq(I);
corr = histcor(I);

figure(1);
subplot(2,1,1)
imshow(origin);
title('Matlab algorithm')
subplot(2,1,2);
imshow(corr);
title('Own implementation')

