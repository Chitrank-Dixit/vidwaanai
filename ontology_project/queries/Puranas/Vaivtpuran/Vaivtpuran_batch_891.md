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

### Verse 1 (Vaivtpuran 543.16134)
- **Original**: भी हैं। क्या जल है और कया स्थल है, मैं यह तुम भव छोड़कर ठीक-ठीक कहना और इस
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.16135)
- **Original**: भी नहीं समझ पाती। मुझे रात-दिनका ज्ञान नहीं उत्तम सभामें सत्य ही बोलना। सौ कुएँसे एक रहता और न मैं अपने-आपको तथा सूर्य- बावली श्रेष्ठ है, सौ बावलियोंसे एक यज्ञ श्रेष्ठ चन्द्रमाके उदयको ही जान पाती हूँ। इस समय है, सौ यज्ञोंसे एक पुत्र श्रेष्ठ है और सौ पुत्रोंसे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.16136)
- **Original**: श्रीहरिका समाचार पाकर क्षणभरके लिये मुझे बढ़कर सत्य है। सत्यसे बढ़कर दूसरा धर्म नहीं
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.16137)
- **Original**: चेतनता आ गयी है। अब मैं श्रीकृष्णके स्वरूपका है और झूठसे बढ़कर दूसरा पाप नहीं है*। दर्शन कर रही हूँ, मुरलीकी ध्वनि सुन रही हूँ उद्धवने कहा--सुन्दरि! सचमुच ही श्रीहरि
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.16138)
- **Original**: तथा कुल, लज्जा और भयका त्याग करके आयेंगे और तुम उनका दर्शन करोगी-यह भी
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.16139)
- **Original**: श्रीहरिके चरणका ध्यान कर रही हूँ। जो समस्त सत्य है। उस समय श्रीहरिके चन्द्रमुखका
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.16140)
- **Original**: लोकोंके ईश्वर तथा प्रकृतिसे परे हैं, उन श्रीहरिको अवलोकन करके निश्चय ही तुम्हारा संताप दूर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.16141)
- **Original**: पाकर भी मायाके बशीभूत होनेके कारण उनको हो जायगा। महाभागे! तुम्हारा विरह-ताप तो मेरे
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.16142)
- **Original**: गोपपति समझकर मैं उन्हें यथार्थरूपसे जान न दर्शनसे हो नष्ट हो गया; अब तुम इस दुस्तर
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.16143)
- **Original**: सकौ। वेद और ब्रह्मा आदि देवता जिनके चिन्ताकों छोड़ो और नाना प्रकारके भोगजनित
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.16144)
- **Original**: चरणकमलोंका ध्यान करते रहते हैं; उन्हींकी मैंने सुखका उपभोग करो। मैं मथुरा जाकर श्रीहरिको
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.16145)
- **Original**: क्रोधमें भरकर भर्त्सना कर दी थी-यह मेरा समझा-बुझाकर यहाँ भेजूँगा। वे अन्य सभी कार्य
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.16146)
- **Original**: बर्ताव मेरे हृदयमें कॉँटेकी तरह चुभ रहा है। चूर्ण करेंगे। मात:! अब मुझे बिदा दो। मैं उद्धव! उनके चरणकमलॉोंकी सेवाओंमें, गुण- श्रीहरिके संनिकट जाऊँगा और यह साग वृत्तान्त
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.16147)
- **Original**: कीर्तनर्में, उनकी भक्तिमें, ध्यान अथवा पूजामें यथोचितरूपसे उन्हें सुनाऊँगा। जो क्षण व्यतीत होता है; उसीमें सारा मड्भल, तब श्रीराधिकाजी बोलीं--वत्स! जब
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.16148)
- **Original**: आनन्द और जीवन स्थित है। उसके विच्छेद तुम परम मनोहर मथुरापुरीको जा रहे हो; तो
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.16149)
- **Original**: हो जानेपर सदा हृदयमें संताप और विप्न होता >073035:/ 2475: समय और उहरो और स्थिरतापूर्वक मेरे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.16150)
- **Original**: है। अब मेरी पुनः उस प्रकारकी अभीष्ट क्रीड़ा- पास बैठो। जरा, मेरी कुछ दुःख-कहानी तो सुनते
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.16151)
- **Original**: प्रीति नहीं होगी, न वैसा प्रेम-सौभाग्य होगा और *न हि सत्यात्‌ परों धर्मों नानृतात्‌ पातक॑ परम्‌
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.16152)
- **Original**: (93। 79)
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.16153)
- **Original**: छ्ग्ड + संक्षिप्त ख्रह्मवैवर्तपुराण « %$4%&% #% 4 &ऋ £; 45444 444; 4; 4; 6 4 44 # % # % # % # ऋ 4 # % % % $ % $ 46 4 4 $ 4 5 4 % 4 4 शक 4 ऋ 45% ऋ ऋ ऊ ्रकअरक 8 8 % न निर्जन स्थानमें समागम ही होगा। उद्धव! अब
- **Translation**: 

---

