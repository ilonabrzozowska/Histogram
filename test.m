RGB = double(imread('images/lena.jpg'));

R = RGB(:,:,1);
G = RGB(:,:,2);
B = RGB(:,:,3);

Y = 0.299 * R + 0.587 * G + 0.114 * B;
U = -0.14713 * R - 0.28886 * G + 0.436 * B;
V = 0.615 * R - 0.51499 * G - 0.10001 * B;

R = Y + 1.139834576 * V;
G = Y -.3946460533 * U -.58060 * V;
B = Y + 2.032111938 * U;

RGB = cat(3,R,G,B)./255;
imshow(RGB); 