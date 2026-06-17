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

### Verse 1 (Vaivtpuran 543.13794)
- **Original**: खींचकर उन्होंने प्रेमपूर्वक्क छातीसे लगा लिया ताड़ोंके बराबर थी तथा कण्ठ, ओठ और तालु और स्वयं भी प्रेमाकुल होकर रो पड़े! सूखे हुए थे। उसके दाँत हरिसके समान लंबे थे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.13795)
- **Original**: बृहस्पतिजीको संतुष्ट तथा रोते देख देवेश्वर इन्द्रका उसने इन्द्रको बहुत डरा दिया। वे जब दौड़ते थे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.13796)
- **Original**: अज्भ-अड्भ पुलकित हो उठा। भक्तिभावसे उनका तो उनके पीछ-पीछे वह भी दौड़ती थी।
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.13797)
- **Original**: मस्तक झुक गया और बे हाथ जोड़कर उनकी ब्रह्महत्या बलिप्ठ थी और इन्द्र अपनी चेतनातक
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.13798)
- **Original**: स्तुति करने लगे।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.13799)
- **Original**: * श्रीकृष्णजन्मखण्ड + 599 6%6%#%%%%ऋ% 55555 54% #### #ऋ#ऋ# ऋ% ऋ#ऋऊ 44 ######ऋकऋककऊऊऋऋऊ कक 44 कक ऊकफकऊऊकऊकफऊ कक कक कक इन्द्र बोले-- भगवन्‌! मेरे अपराधको क्षमा
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.13800)
- **Original**: बृहस्पतिने शिष्पको उस कवचका उपदेश दिया कीजिये। कृपानिधान! कृपा कौजिये। अच्छे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.13801)
- **Original**: और अनायास ही हुझ्भारमात्रसे ब्रह्महत्याकों भस्म स्वामी अपने सेवकके अपराधको हृदयमें स्थान
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.13802)
- **Original**: कर डाला। तदनन्तर शिष्यको साथ लेकर नहीं देते। अपनी पत्नी, अपने शिष्य, अपने भृत्य
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.13803)
- **Original**: बृहस्पतिजी अमरावतीपुरीमें गये। इन्द्रने गुरुकी तथा अपने पुत्रोंको दुर्बल या सबल कौन मनुष्य
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.13804)
- **Original**: आज्ञासे उस पुरीकी दशा देखी। शत्रुने उस दण्ड देनेमें असमर्थ होता है? तीन करोड़
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.13805)
- **Original**: नगरीकों तोड़-फोड़ डाला था। देवताओंमें मैं ही एक देवाधम और मूढ़ हूँ।। . पतिका आगमन सुनकर शचीके मनमें बड़ा सुरश्रेष्ट! आपकी कृपासे ही मैं उच्च पदपर
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.13806)
- **Original**: हर्ष हुआ। उसने भक्तिभावसे गुरुदेबको प्रणाम प्रतिष्ठित हूँ। आपने ही दया करके मुझे आगे करके प्राणवल्लभके चरणोंमें भी मस्तक झुकाया। बढ़ाया है। आप सारे जगत्‌का संहार करनेको
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.13807)
- **Original**: प्रिये! इन्द्रका शुभागमन सुनकर सब देवता, ऋषि शक्ति रखते हैं। आपके सामने मेरी क्या बिसात
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.13808)
- **Original**: और मुनि वहाँ आये। उनका चित्त हर्षसे गद़द है? मैं वैसा ही हूँ, जैसा बावलीका कौट। आप
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.13809)
- **Original**: हो रहा था। इन्द्रने अमराबतीका निर्माण करनेके साक्षात्‌ विधाताके पौत्र हैं; अत: स्वयं दूसरी सृष्टि
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.13810)
- **Original**: लिये एक श्रेष्ठ देवशिल्पीको नियुक्त किया। रचनेमें समर्थ हैं। देवशिल्पीने पूरे सौ बर्षोत्क अमराबतीकी रचना इन्द्रके मुखसे यह स्तबन सुनकर गुरु
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.13811)
- **Original**: की। नाना विचित्र रत्नोंसे सम्पन्न तथा श्रेष्ठ बृहस्पति बहुत संतुष्ट हुए। उनके मुख और नेत्र
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.13812)
- **Original**: मणिरत्रोंद्वारा निर्मित उस मनोहर पुरीकी कहीं प्रसन्नतासे खिल उठे और बे प्रेमपूर्वक बोले।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.13813)
- **Original**: उपमा नहीं थी। फिर भी उससे देवराज इन्द्र बृहस्पतिने कहा--महाभाग! धैर्य धारण
- **Translation**: 

---

