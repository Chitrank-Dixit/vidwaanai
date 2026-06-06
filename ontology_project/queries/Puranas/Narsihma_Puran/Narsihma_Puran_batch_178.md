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

### Verse 1 (Narsihma Puran 0.3541)
- **Original**: 125 रामो5पि दग्ध्वा तबेहँ स्नातो दत्त्वा जलाझलिमू
- **Translation**: 

---

### Verse 2 (Narsihma Puran 0.3542)
- **Original**: ्रात्रा सगच्छन्‌ दुःखातों राक्षसी पथि दृष्टवान्‌
- **Translation**: 

---

### Verse 3 (Narsihma Puran 0.3543)
- **Original**: 126 उद्वमन्ती महोल्काभां विवृत्तास्यां भवंकरीम्‌। क्षय नयन्तीं जन्तून्‌ बै पातयित्वा गतों रुषा
- **Translation**: 

---

### Verse 4 (Narsihma Puran 0.3544)
- **Original**: 127 गच्छन्‌ वनान्तरं राम: स कब॒न्ध॑ दरदर्श ह। बिरूप जठरमुखं दीर्घवाहूं घनस्तनम्‌
- **Translation**: 

---

### Verse 5 (Narsihma Puran 0.3545)
- **Original**: 128 रुन्धानं राममार्ग तु दृष्ठा त॑ं दग्धवाञ्शनैः
- **Translation**: 

---

### Verse 6 (Narsihma Puran 0.3546)
- **Original**: दग्धोउसी दिव्यरूपी तु खस्थो राममभाषत
- **Translation**: 

---

### Verse 7 (Narsihma Puran 0.3547)
- **Original**: 129 राघप राम महावाहों त्ववा मम महामते। विरूप॑ नाशितं बीर मुनिशापाच्यिरागतम्‌
- **Translation**: 

---

### Verse 8 (Narsihma Puran 0.3548)
- **Original**: 130 ब्रिदिवं यामि ध्रन्योउस्मि त्वग्यसादात्र संशय: । त्ब॑ सीताप्राम्ये सख्यं कुरु सूर्यसुतेत भो:
- **Translation**: 

---

### Verse 9 (Narsihma Puran 0.3549)
- **Original**: 131 बानरेद्रेण गत्वा तु सुग्रीबे स्व॑ निवेद्य वै। भविष्यति नृपश्रेष्ठ ऋष्यमूकगिरिं श्रज
- **Translation**: 

---

### Verse 10 (Narsihma Puran 0.3550)
- **Original**: 132 इत्युकत्वा तु गते तस्मिन्‌ रामो लक्ष्मणसंयुत:
- **Translation**: 

---

### Verse 11 (Narsihma Puran 0.3551)
- **Original**: सिद्धैस्तु मुनिभि: शून्यमाश्रमं प्रविवेश ह
- **Translation**: 

---

### Verse 12 (Narsihma Puran 0.3552)
- **Original**: 133 तत्रस्थां तापसी दृष्टा तया संलाप्य संस्थित: । शबरीं मुनिमुख्यानां सपर्याहतकल्मषाम्‌
- **Translation**: 

---

### Verse 13 (Narsihma Puran 0.3553)
- **Original**: 134 तया सम्पूजितो रामों बदरादिभिरीश्वर:। साप्येनं पूजयित्वा तु स्वामवस्थां निवेद्य बै।। 135 सीतां त्व॑ प्राप्स्यसीत्युकत्वा प्रविज्यात्रिं दिवंगता। दिवं प्रस्थाप्य तां चापि जगापान्यत्र राघय:
- **Translation**: 

---

### Verse 14 (Narsihma Puran 0.3554)
- **Original**: 136 तदनन्तर जठायु अपना शरोर त्यागकर एक सुन्दर विमानपर आउज हुए और अप्सरागणोंसे सेवित हो स्वर्गलोककों चले गये। श्रीरामचन्द्रजीने भी उनके शरोरका दाह-संस्कार करके स्तानके पश्चात्‌ उनके निमित जलाझलि दी। फिर सौताके लिये दुःखो हो भाई लक्ष्मणके साथ आगे जाने लगे। इतनेमें हो उन्हें सस्तेपर एक राक्षसों खड़ी दिखायी दी। बह मुँहसे बड़ी भारो उल्काफे समान आगकी ज्वाला डाल रही थी। उसका मुँह फैला हुआ था। वह बड़ी डरावतों थो ओर पास आये हुए अनेकानेक जोबोंका संहार कर रहो थो। श्रीशामत्रे उसे रोषपूर्वक मार गिए्या। फिर ये आगे बढ़ गये। जब श्रीराम दूसरे जनमें जाने लगे, तब उन्होंने कबन्थको देखा, जो बहुत हो कुरूप था। उसका मुख उसके पेटमें ही था, याँहें बड़ी-बड़ी थीं और स्तन घने थे। श्रीयमने उसे अपना मार्ग ग्रेकते देख उसे काठ-कब्राइद्वारा धीरे-घोरे जला दिया। जल जानेपर यह दिव्यरूप थारण करके प्रकट हुआ और आकाज्ञमें स्थित होकर श्रीरामसे बोला--
- **Translation**: 

---

### Verse 15 (Narsihma Puran 0.3555)
- **Original**: 124--129
- **Translation**: 

---

### Verse 16 (Narsihma Puran 0.3556)
- **Original**: *महाप्राहु श्रोराम
- **Translation**: 

---

### Verse 17 (Narsihma Puran 0.3557)
- **Original**: महामते वीरवर ! एक मुनिके शापवश चिरकालसे प्राप्त हुई मेरी कुरूपताकों आपने नष्ट कर दिया; अब मैं स्वर्गलोकको जा रहा हूँ। इसमें संदेह नहों कि आज मैं आपकी कृपासे धन्य हो गया। रघुनन्दव ! आप सोताकी ग्राप्तिक लिये सूर्यकृमार वानरणज सुग्रीकके साथ मित्रता कीजिये
- **Translation**: 

---

### Verse 18 (Narsihma Puran 0.3558)
- **Original**: उनके यहाँ जाकर सुग्रीवसे सारा वृत्तान्त निवेदन कर देनेपर आपका कार्य सिद्ध हो जायगा। अत: -नृपश्रे
- **Translation**: 

---

### Verse 19 (Narsihma Puran 0.3559)
- **Original**: ्र! आप सहाँसे ऋष्यमूक पर्वतपर जाइये'
- **Translation**: 

---

### Verse 20 (Narsihma Puran 0.3560)
- **Original**: 130--132
- **Translation**: 

---

