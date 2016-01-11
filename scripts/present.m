function [] = present(origin, corr)

figure(1);
subplot(2,1,1)
imshow(origin);
title('Matlab algorithm')
subplot(2,1,2);
imshow(corr);
title('Own implementation')

