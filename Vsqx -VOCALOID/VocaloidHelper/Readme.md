<h1>VOCALOID Helper</h1>
<h2>概述</h2>
VOCALOID Helper解决P主调曲时VOCALOID编辑器不支持所有音符等比例伸长、并放置在等比例的新位置上的问题。<br>
简而言之， 则是帮助P主放慢歌姬歌唱速度。<br>
<h2>原理</h2>
VOCALOID工程文件*.vsqx实质为XML标签文件。 因此对其中所有音符/片段的"dur""t"等标签中对持续时间描述的修改实现对歌唱速度的调节。<br>
<h2>Version 1版本说明</h2>
<h3>概述</h3>
<b>源码（Python3）：</b><a href="https://github.com/xiawenke/MyCodes/raw/master/Vsqx%20-VOCALOID/VocaloidHelper/Version1.py">Version1.py</a><br>
<b>打包的exe（可直接在Windows平台执行）</b><a href="https://github.com/xiawenke/MyCodes/blob/master/Vsqx%20-VOCALOID/VocaloidHelper/VocaloidHelperVersion1.exe?raw=true">VocaloidHelper/VocaloidHelperVersion1.exe</a><br>
<h3>V1使用教程</h3>
· 在Windows平台下运行VocaloidHelperVersion1.exe（或者在Python3环境下Run 源代码）<br>
· 在短暂等待加载后会看到命令行出现以下内容：<br>
  &nbsp; &nbsp; &nbsp; &nbsp; <code>Vsqx File: &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; </code><br>
· 接着， 向命令行拖入vsqx文件：<br>
<img src="http://static.miku-miku.online/images/github.com.vocaloidhelper.png" /><br>
  &nbsp; &nbsp; &nbsp; &nbsp;<code>Vsqx File: "C:\Users\FrankXia\Documents\Python Scripts\VocaloidHelper\test\test.vsqx"</code><br>
· 点击回车“Stretch Parameter (Recommand to input 0.75 here):”。这里指的是调整之后的歌唱速度×（乘以）Stretch Parameter则是调整之前的速度。 （如果想要优化音源建议这里填写0.75）<br>
· 再次回车， 等待， 即可得到结果。<br>
<img src="http://static.miku-miku.online/images/github.com.vocaloidhelper1.png" />
