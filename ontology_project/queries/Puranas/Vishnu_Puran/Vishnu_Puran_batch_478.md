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

### Verse 1 (Vishnu Puran 0.9541)
- **Original**: आप अपने उस स्वरूपका स्मरण कीजिये जो समस्त संसास्का कारण तथा क्ारणका भी पूर्ववर्ती है और प्रलयकालमें भी स्थित रहनेवाला है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9542)
- **Original**: क्या आपको मालूम नहीं है कि आप और मैं दोनों ही इस संसारके एकमात्र कारण हैं और पृथिवीका भार उतारनेके लिये ही मर्त्यलोकमें आये हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9543)
- **Original**: हे अनन्त ! आकाश आपका सिर है, मेघ केदा
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9544)
- **Original**: सोमो मनस्ते श्रसितं समीरणो दिशश्षतस्रोौउव्यय बाहवस्ते
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9545)
- **Original**: 26 सहस्लवकक्‍्त्रो.. भगवन्महात्पा सहस्रहस्ताइप्रिशरीरभेद:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9546)
- **Original**: सहस्रपझोद्धवयोनिराद्य- स्सहस्लशास्त्वां मुनयो गृणन्ति
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9547)
- **Original**: 27 दिव्यं हि रूप॑ तब वेत्ति नान्‍यो तदर्व्यते वेत्सि न कि यदन्ते त्वय्येव विश्व लयमभ्युपैति
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9548)
- **Original**: 28 सहल्लपः निमेषपूर्वो जगदेतदत्सि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9549)
- **Original**: 29 अत्ते यथा बाडववहिनाम्बु हिमस्वरूप॑ परिगृह्य कास्तप' । हिमाचले भानुमतों5शुसड्जा- जलवत्वमभ्येति पुनस्तदेव
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9550)
- **Original**: 30 एवं ल्वया संहरणेउत्तमेत- ज्जगत्समस्त॑ त्वदधीनकं पुनः । तवैव॒ सर्गाय समुद्यतस्य जगर््वमभ्येत्यनुकल्पममीश
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9551)
- **Original**: 31 भ्वानह च विश्वात्मन्नेकमेब च्॒ कारणम्‌। जगतो5स्य जगत्यर्थे भेदेनावां व्यवस्थितो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9552)
- **Original**: 32 तत्स्मर्यताममेयात्मंस्त्वयात्मा जहि दानवम्‌। मानुष्यपेवावलम्ब्य बन्यूनां क्रियतां हितम्‌
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9553)
- **Original**: 33 श्षीपरशर उवाच इति संस्मारितो विप्र कृष्णेन सुमहात्मना । विहस्प पीडयापमास प्रलाम्बे बलवान्ब॒लः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9554)
- **Original**: 34 मुष्टिना सो5हनन्यून्नि कोपसंरक्तलोचन: । तेन चास्य प्रहारेण अहियाति विलछोचने
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9555)
- **Original**: 35 1. कम्‌ अस्तम-प्रक्षितम्‌। अश्रीविष्णुपुराण [ अ* 9 हैं, पृथिवी चरण हैं, अग्रि मुख है, चन्द्रमा मन हैं, जायु श्वास-प्रधास हैं और चारों दिद्याएँ बाहु हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9556)
- **Original**: है भगवन्‌ ! आप महाकाय हैं, आपके सहस्ल्र मुख हैं तथा सहस्नों हाथ, पाँव आदि शरीस्के भेद हैं। आप सहस्लों ब्रह्माओंकि आदिकारण हैं, मुनिजन आपका सहसतों च्रकार वर्णन करते हैं
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9557)
- **Original**: आपके दिव्य रूपको ( आपके अतिरिक ] और कोई नहीं जानता, अतः समस्त देवगण आपके अवताररूपकी ही उपासना करते हैं। कया आपको बिदित नहीं है कि अन्तमें यह सम्पूर्ण विश्व आपहीमें लीन हो जाता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9558)
- **Original**: हे अनन्तमूर्ते ! आपहीसे धारण की हुई यह पृथिवी सम्पूर्ण चराचर विश्रकों धारण करती हैं। है अज! निमेषादि कालस्वरूप आप ही कृतयुग आदि भेदोंसे इस जगत्का ग्रास करते हैं
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9559)
- **Original**: जिस प्रकार बढ़वानलसे पीया हुआ जल बायुद्रारा हिसालयतक पहुँचाये जानेपर हिसका रूप धारण कर लेता है और फिर सूर्य-किरणोंका संयोग होनेसे जलरूप हो जाता है उसी प्रकार हे ईद ! यह समस्त जगत्‌ [ रूद्रादिख्पयसे ] आपलीके द्वारा थिनष्ट होकर आप [ परमेश्वर ] के ही अधीन रहता है और फिर प्रत्येक कल्पमें आफ्के [ हिरण्यगर्भरूपसे ] सृष्टि रचनामें प्रवृत्त होनेपर यह [ विरादरूपसे ] स्थूल जगदूुप हो जाता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9560)
- **Original**: हे विश्वात्मन्‌! आप और मैं दोनों ही इस जगत्‌के एकमात्र कारण हैं संसारके हितके लिये ही हमने भिन्न-भिन्न रूप धारण किये हैं
- **Translation**: 

---

