# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 13.10542)
- **Original**: कि तुम लोग श्रेष्ठ वैष्णव हो और अपने चरणकमलोंकी कमलसे पूजा करते हैं, आज साक्षात्‌ उन्हींको
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.10543)
- **Original**: धूलसे पृथ्वीको पवित्र करनेके लिये भ्रमण कर रहे कमल अर्पण करके हम सब-के-सब पतवित्र हो हो। मैं श्रीकृष्णभक्तके दर्शनकी सदा ही इच्छा गये। प्रभो! ब्रह्म एक ही है, दूसरा नहीं है। करता रहता हूँ; क्योंकि साधु-संत तीनों लोकोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.10544)
- **Original**: ड72 + संक्षिम ब्रह्मयैवर्तपुराण « ##6#4## 4 ## 64 #### 4 ## ## #### 444 4 8 5 $ 5 5 5 4 * 5 $ 5 5 5 5 4 % ऋ ऋ 45% 4 # $% 8 #& 8 #& 8 $ # % 5 55 5 5 55 दुर्लभ हैं। तुम लोग मुझे पार्वती और देवताओंसे
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.10545)
- **Original**: मैं यह सुनना चाहता हूँ कि पार्वतीने कौन- भी बढ़कर सदा प्रिय हो। मुझे वैष्णवजन अपने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.10546)
- **Original**: सा व्रत किया था? उस ब्रतके आराध्यदेव कौन तथा अपने भक्तोंसे भी अधिक प्रिय हैं। परंतु मैंने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.10547)
- **Original**: हैं? उसका फल क्या है और उसमें पालन पूर्वकालमें जो प्रतिज्ञा कर रखी है, बह भी व्यर्थ
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.10548)
- **Original**: करनेयोग्य नियम क्‍या है? भगवन्‌! उस ब्रतके नहीं होनी चाहिये। महाभाग बैष्णवो! सुनो। मैंने
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.10549)
- **Original**: लिये उपयोगी. द्रव्य कौन-कौन-से हैं? कितने कह रखा है कि पार्वतीके ब्रतके समय जो लोग
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.10550)
- **Original**: समयतक वह ब्रत किया जाता है और उसको किसी अन्य ब्रतके निमित्त इस सरोवरसे कमल ले
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.10551)
- **Original**: प्रतिष्ठामें क्या-क्या करना आवश्यक होता है? जायँगे वे शीघ्र ही आसुरी योनिकों प्राप्त होंगे,
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.10552)
- **Original**: प्रभो! भलीभाँति विचारकर बताइये। इसे सुननेके इसमें संशय नहीं है। श्रीकृष्णके भक्तोंका कहीं भी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.10553)
- **Original**: लिये मेरे मनमें बड़ा कौतूहल है। अशुभ नहीं होता है। तुम लोग पहले दानवी
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.10554)
- **Original**: . श्रीनारायण बोले--मुने ! यह 'त्रैमासिक' योनिमें पड़कर फिर निश्चय ही गोलोकमें पधारोगे। नामक ब्रत है, जो नारीके पतिविषयक सौभाग्यको तुम्हारे मनमें श्रीकृष्णके रूपका प्रत्यक्ष दर्शन बढ़ानेवाला है। इस ब्रतके आराध्य देवता करनेके लिये उत्कण्ठा है। अत: बच्चो! तुम्हें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.10555)
- **Original**: हैं--राधिकासहित भगवान्‌ श्रीकृष्ण। उत्तरायणके भारतवर्षके वृन्दावनमें उस रूपका अवश्य दर्शन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.10556)
- **Original**: विषुव योगमें इसका आरम्भ होता है और होगा। श्रीकृष्णको देखकर उन्हींके हाथसे मृत्युको
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.10557)
- **Original**: दक्षिणायन आरम्भ होनेतक इसकी समाप्ति हो प्राप्त हो तुम वैष्णवशिरोमण बन जाओगे और
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.10558)
- **Original**: जाती है। वैशाखकी संक्रान्तिसि एक दिन पहले दिव्य विमानपर आरूढ़ हो हरिधामको पधारोगे।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.10559)
- **Original**: संयमपूर्वक रहकर निश्चय ही हविष्यका सेवन तुम लोग अभी यहाँ उस वाब्छनीय रूपको
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.10560)
- **Original**: करे। फिर वैशाखको संक्रान्तिके दिन स्नान करके देखनेके लिये उत्सुक हो। अत: वह सब देखो।'
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.10561)
- **Original**: गड्भातटपर ब्रतका संकल्प ले। तदनन्तर ब्रती ऐसा कहकर भगवान्‌ शिवने उन्हें उस
- **Translation**: 

---

