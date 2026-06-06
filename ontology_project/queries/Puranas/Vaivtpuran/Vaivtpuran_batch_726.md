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

### Verse 1 (Vaivtpuran 543.12834)
- **Original**: सोते शंकरकों सींगोंसे उठाया और उन्हें अपना समय मेरी आज्ञासे बह असुर तुरंत मायाद्वारा
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.12835)
- **Original**: कबच तथा शत्रुमर्दन शूल दिया। उसे पाकर ठगा गया। (मैंने उसको यह कहकर मोहमें डाल
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.12836)
- **Original**: उन्होंने दानवोंके उस अत्यन्त ऊँचे स्थान दिया कि तुम अपने सिरपर हाथ रखकर परीक्षा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.12837)
- **Original**: त्रिपुरकों, जो आकाशमें निराधार टिका हुआ था, तो करो कि यह बात सत्य है या नहीं।) उसने
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.12838)
- **Original**: मेरे दिये हुए शूलसे नष्ट कर दिया। इसके बाद अपने मस्तकपर हाथ रखा और तत्काल जलकर
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.12839)
- **Original**: शिवने मुझ दर्पहन्ताका ही बारंबार लज्जापूर्वक भस्म हो गया। तब सिद्ध, सुरेन्द्र, मुनौन्र और
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.12840)
- **Original**: स्तवन किया। दैत्यराज त्रिपुर उसी क्षण चूर- मनु प्रसन्नतापूर्वक उत्तम भक्तिभावसे मेरी स्तुति
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.12841)
- **Original**: चूर होकर पृथ्वोपर गिर पड़ा। यह देख सब करने लगे और शिवजी लज्जित हो गये। उनका
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.12842)
- **Original**: देवता और मुनि प्रसन्नतापूर्वक शिवजीकी स्तुति गर्व चूर्ण हो गया। फिर मैंने उन्हें समझाया और करने लगे। तबसे भगवान्‌ शंकरने विप्रके वे अपने स्थानकों गये।
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.12843)
- **Original**: बीजस्वरूप दर्पको त्याग दिया। वे ज्ञानानन्दस्वरूपसे इसी तरह गर्वमें भरे हुए रुद्र भधानक असुर
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.12844)
- **Original**: स्थित हो सब कर्मामें निर्लिप्तभावसे संलग्र रहने त्रिपुरका वध करनेके लिये गये। वे मन-ही-
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.12845)
- **Original**: लगे। तदनन्तर मैं अपने प्रिय भक्त शंकरको मन यह समझकर कि 'मैं तो समस्त लोकोंका
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.12846)
- **Original**: वृषरूपसे पीठपर बहन करने लगा; क्योंकि तीनों संहारक हूँ, फिर मेरे सामने इस पतिंगेके समान
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.12847)
- **Original**: लोकोंमें शिवसे बढ़कर प्रियतम मेरे लिये दूसरा
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.12848)
- **Original**: 562 « संक्षिप्त ब्रह्मवैयर्तपुराण * %##&##$ $ # # हक 4 / कक कक 4 ऋ 4 $ 5 # कक कक 5 #$ 5 #ऊ कक क# # # # 4 # कक $ हक कक भर # 5 $ हड कोई नहीं है*। ब्रह्मा मेरे मनस्वरूप, महेश्वर मेरे
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.12849)
- **Original**: ही तुल्य महान्‌ हैं। फिर वे अपने सारे अद्लोंमें ज्ञानरूप और मूलप्रकृति ईश्वरी भगवती दुर्गा मेरी
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.12850)
- **Original**: विभूति क्‍यों लगाते हैं? पद्ममुख और त्रिलोचन बुद्धिरूपा हैं। निद्रा आदि जो-जो शक्तियाँ हैं, क्यों कहलाते हैं? दिगम्बर और जटाधारी क्‍यों वे सब-कौ-सब प्रकृतिकी कलाएँ हैं। साक्षात्‌
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.12851)
- **Original**: हैं? सर्प-समुदायसे क्यों विभूषित होते हैं? वे सरस्वती मेरी वाणीकी अधिष्ठात्री देवी हैं।
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.12852)
- **Original**: देवेद्ध श्रेष्ठ वाहन छोड़कर वृषभके द्वारा क्‍यों कल्याणके अधिदेवता गणेशजी मेरे हर्ष हैं। स्वयं
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.12853)
- **Original**: भ्रमण करते हैं ? रत्नसारनिर्मित आभूषण क्‍यों नहीं धर्म परमार्थ है तथा अग्रिदेव मेरे भक्त हैं;
- **Translation**: 

---

