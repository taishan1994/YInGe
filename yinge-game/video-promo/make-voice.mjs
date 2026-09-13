import { ttsSave } from './node_modules/edge-tts/out/index.js';

const text = '音格，一款把拼音组词和棋盘策略结合在一起的多人桌游。每轮抽取声母、韵母、整体认读和万能牌，先拼出音节，再选择对应汉字。把新词接在棋盘已有的词旁边，横向、纵向或交叉连接，都可以得分。特殊格会让分数翻倍，连接越巧妙，收益越高。想不到怎么下时，点击提示最高分，系统会预填当前最优方案。你也可以撤销本轮、换牌，或者直接跳过。支持朋友对战，也支持和电脑对战。拼出好词，赢下棋盘，这就是音格。现在开始你的对局。';
await ttsSave(text, './voice-neural.mp3', {
  voice: 'zh-CN-XiaoxiaoNeural',
  rate: '-8%',
  pitch: '+0Hz',
  volume: '+0%'
});
