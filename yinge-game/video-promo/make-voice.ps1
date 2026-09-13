Add-Type -AssemblyName System.Speech
$s = New-Object System.Speech.Synthesis.SpeechSynthesizer
$s.SelectVoice('Microsoft Huihui Desktop')
$s.Volume = 100
$ssml = @'
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="zh-CN">
  <prosody rate="-8%">音格，</prosody><break time="350ms"/><prosody pitch="+2st" rate="-4%">把拼音组词和棋盘策略，结合在一起。</prosody>
  <break time="500ms"/><prosody rate="-6%">每轮抽取声母、韵母、整体认读和万能牌，先拼出音节，再选择对应汉字。</prosody>
  <break time="450ms"/><prosody pitch="+1st" rate="-8%">把新词接在棋盘已有的词旁边，横向、纵向或交叉连接，都可以得分。</prosody>
  <break time="400ms"/><prosody rate="-5%">特殊格会让分数翻倍，连接越巧妙，收益越高。</prosody>
  <break time="550ms"/><prosody pitch="+2st" rate="-5%">想不到怎么下？点击提示最高分。</prosody>
  <break time="300ms"/><prosody rate="-7%">系统会预填当前最优方案。你也可以撤销本轮、换牌，或者直接跳过。</prosody>
  <break time="500ms"/><prosody pitch="+1st" rate="-5%">支持朋友对战，也支持和电脑对战。</prosody>
  <break time="450ms"/><prosody pitch="+2st" rate="-8%">拼出好词，赢下棋盘。</prosody><break time="350ms"/>这就是音格。
</speak>
'@
$s.SetOutputToWaveFile((Join-Path $PSScriptRoot 'voice-emotive.wav'))
$s.SpeakSsml($ssml)
$s.Dispose()
