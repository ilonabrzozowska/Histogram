function img = hist_processings(I)
[rows,columns,channels] =  size(I);

if channels == 1
  img = histcor(I);

else
  yuv = rgb2yuv(I);
  ui = yuv(:,:,1);
  ui = ui.*255;
  ui = uint8(ui);
  ui = histcor(ui);
  yuv(:,:,1) = double(ui)./255;
  img = yuv2rgb(yuv);
end
imwrite(img,'tmp.png');
end
 