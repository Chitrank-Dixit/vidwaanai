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

### Verse 1 (Vaivtpuran 6.9311)
- **Original**: थे। चन्दन, अगुरु तथा कस्तूरीद्वारा रचित चित्रपत्रक विराजमान, पारिजात-पुष्पोंके मालाजालसे सुशोभित,
- **Translation**: 

---

### Verse 2 (Vaivtpuran 6.9312)
- **Original**: उनके भाल और कपोलको विभूषित कर रहे थे। सहस्र पहियोंसे युक्त, मनके समान तीव्रगामी और
- **Translation**: 

---

### Verse 3 (Vaivtpuran 6.9313)
- **Original**: नूतन बन्धुजीव-पुष्पके समान आभावाले लाल- मनोहर था। ग्रीष्म-ऋतुके मध्याह्कालिक मार्तण्डको
- **Translation**: 

---

### Verse 4 (Vaivtpuran 6.9314)
- **Original**: लाल ओठके कारण उनके मुखकी शोभा और भी प्रभाको तिरस्कृत करनेवाला वह श्रेष्ठ विमान
- **Translation**: 

---

### Verse 5 (Vaivtpuran 6.9315)
- **Original**: बढ़ गयी थी। उनकी दन्तावली मोतियोंकी मोती, माणिक्य और हौरोंके समूहसे जाज्वल्यमान
- **Translation**: 

---

### Verse 6 (Vaivtpuran 6.9316)
- **Original**: पाँतकी प्रभाको लूटे लेती धी। प्रफुल्ल मालतीकी जान पड़ता था। उसमें विचित्र पुतलियों, पुष्प,
- **Translation**: 

---

### Verse 7 (Vaivtpuran 6.9317)
- **Original**: मालासे अलंकृत बेणी धारण करनेवाली बे देवी सरोवरों और काननोंसे उसकी अद्भुत शोभा हो
- **Translation**: 

---

### Verse 8 (Vaivtpuran 6.9318)
- **Original**: बड़ी ही सुन्दर थीं। गरुड़की चोंचके समान रही थी। मुने! बह देवताओं और दानवोंके रथोंसे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 6.9319)
- **Original**: नुकीली नासिकाके अग्रभागमें लटकती हुई बहुत बड़ा था। भगवान्‌ शंकरकी प्रसतन्नताके लिये
- **Translation**: 

---

### Verse 10 (Vaivtpuran 6.9320)
- **Original**: गजमुक्ताकी बुलाक अपूर्व छटा बिखेर रही थी। विश्वकर्माने यत्रपूर्वक्त उस दिव्य रथका निर्माण
- **Translation**: 

---

### Verse 11 (Vaivtpuran 6.9321)
- **Original**: अग्रिशुद्ध एवं अत्यन्त दीप्िमान्‌ वस्त्रसे वे उद्धासित किया था। वह पचास योजन ऊँचा और चार
- **Translation**: 

---

### Verse 12 (Vaivtpuran 6.9322)
- **Original**: हो रही थीं और दोनों पुत्रोंक साथ सिंहकी योजन विस्तृत था। रतिशय्यासे युक्त सैकड़ों
- **Translation**: 

---

### Verse 13 (Vaivtpuran 6.9323)
- **Original**: पीठपर बैठी थीं। उस रथसे उतरकर पुत्रोंसहित प्रासाद उसकी शोभा बढ़ाते थे। उस विमानमें
- **Translation**: 

---

### Verse 14 (Vaivtpuran 6.9324)
- **Original**: देबीने शीघ्रतापूर्वक श्रीकृष्णकों प्रणाम किया। बैठी हुई मूलप्रकृति ईश्वरी देवी दुर्गाकों भी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 6.9325)
- **Original**: फिर वे एक श्रेष्ठ आसनपर बैठ गयीं। इसके बाद देवताओंने देखा, जो रत्रमय अलंकारोंसे विभूषित
- **Translation**: 

---

### Verse 16 (Vaivtpuran 6.9326)
- **Original**: गणेश और कार्तिकेयने परात्पर श्रीकृष्ण, शंकर, थीं और अपनी दिव्य दीप्तिसे तपाये हुए सुवर्णके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 6.9327)
- **Original**: धर्म, संकर्षण तथा ब्रह्माजीकों नमस्कार किया।
- **Translation**: 

---

### Verse 18 (Vaivtpuran 6.9328)
- **Original**: ड22 + संक्षिप्त ब्रह्मवैय्तपुराण +* $5#%%$% 4 ऋ 4 % $ 5 ऋ कक ##ह # ऊ कक कह # 4 ##& 848 68%
- **Translation**: 

---

### Verse 19 (Vaivtpuran 6.9329)
- **Original**: 8& 84 # 85 5 $ 55% 5 4 5 4 5 5 4 4 5 4 4 8 4 4 # 8 88 8 # 5 55 उन दोनों देवेश्वरॉँको निकट आया देख वे सब
- **Translation**: 

---

### Verse 20 (Vaivtpuran 6.9330)
- **Original**: जायँगे। कंसका साक्षात्कार होनेमात्रसे तुम पुनः देवता उठकर खड़े हो गये। उन्होंने आशौर्वाद
- **Translation**: 

---

