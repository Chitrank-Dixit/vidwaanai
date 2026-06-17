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

### Verse 1 (Vaivtpuran 13.11962)
- **Original**: भक्तोंकी रक्षामें लगा रखा है, तथापि उन्हें उसपर बलपर श्रीहरिके दासकों शाप देने गये थे?
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.11963)
- **Original**: पूरा भरोसा नहीं होता। इसलिये वे स्वयं उनकी जिसके रक्षक भगवान्‌ हैं, उसको तीनों लोकोंमें
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.11964)
- **Original**: रक्षा करनेके लिये जाते हैं। उनके मुँहसे अपने कौन मार सकता है? भक्तवत्सल श्रोहरिने छोटे-
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.11965)
- **Original**: गुणों और नामोंका श्रवण करके उन्हें बड़ा आनन्द बड़े सभी भक्तोंकी रक्षाके लिये सुदर्शनचक्रको
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.11966)
- **Original**: मिलता है। इसलिये भगवान्‌ भक्तके साथ सदा सदा नियुक्त कर रखा है। जो मूढ़ श्रीविष्णुके छायाकी तरह घूमते रहते हैं। अत: ब्राह्मणदेव! लिये प्राणोंके समान प्रिय वैष्णव भक्तसे द्वेष गोविन्दका भजन करो। उनके चरणकमलोंका रखता है, उसका संहार भगवान्‌ विष्णु स्वयं करते
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.11967)
- **Original**: चिन्तन करो। श्रीहरिके स्मरणमात्रसे भी सारी हैं। वे श्रीहरि संहारकर्ताका भी संहार करनेमें
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.11968)
- **Original**: आपत्तियाँ नष्ट हो जाती हैं। अब शीघ्र ही समर्थ हैं। अत: बेटा! तुम शीघ्र किसी दूसरे
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.11969)
- **Original**: बैकुण्ठधाममें जाओ। उस धामके अधिपति श्रीहरि स्थानमें जाओ। अब यहाँ तुम्हारी रक्षा नहीं हो
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.11970)
- **Original**: ही तुम्हारे शरणदाता हैं। वे प्रभु दयाके सागर हैं; सकती। यदि नहीं हटे तो सुदर्शनचक्र मेरे साथ
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.11971)
- **Original**: अतः तुम्हें अवश्य ही अभयदान देंगे। ही तुम्हाशा बध कर डालेगा। ये बातें हो ही रही थीं कि सारा कैलास ब्रह्माजीको बात सुनकर ब्राह्मणदेवता दुर्बासा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.11972)
- **Original**: चक्रके तेजसे व्याप्त हो उठा, जैसे समस्त
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.11973)
- **Original**: + श्रीकृष्णजन्मखण्ड * 529 ऋ%%#%##%####&### 4 ######4#$%$5%%%ऊऋऊ कक कं 4 कक कक ऋऋ कक कक 2.0... 3.0. ..).
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.11974)
- **Original**: भूमण्डल सूर्यकी किरणोंसे उद्दीप्त हो उठा हो सुननन्‍्द, नन्‍्द, कुमुद और प्रचण्ड आदि पार्षद उस समय सम्पूर्ण कैलासवासी उस चक्रकी
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.11975)
- **Original**: उन्हें घेरकर खड़े थे। ऐसे प्रभुको देख दुर्वासाने विकराल ज्वालासे संतप्त हो 'त्राहि-त्राहि' पुकारते
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.11976)
- **Original**: दण्डकी भाँति पृथ्वीपर पड़कर प्रणाम किया और हुए भगवान्‌ शंकरकी शरणमें गये। उस दुःसह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.11977)
- **Original**: सामवेदवर्णित स्तुतिके द्वारा उन परमेश्वरका चक्रको देख पार्वतीसहित करुणानिधान भगवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.11978)
- **Original**: स्तवन किया। शंकरने ब्राह्मणको प्रेमपूर्वक आशोीर्वाद देते हुए. दुर्बासा बोले--कमलाकान्त! मेरी रक्षा कहा--' यदि तेज सत्य है और चिरकालसे संचित
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.11979)
- **Original**: कौजिये। करुणानिधे! मुझे बचाइये। प्रभो! आप तप सत्य है तो अपराध करके भयभीत हुआ
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.11980)
- **Original**: दीनोंके बन्धु और अत्यन्त दुःखियोंके स्वामी हैं। यह ब्राह्मण संतापसे मुक्त हो जाय।' दयाके सागर हैं। बेद-वेदाड्रोंके स्रष्टा विधाताके पार्वती बोलीं--यह ब्राह्मण मेरे स्वामीके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.11981)
- **Original**: भी विधाता हैं। मृत्युकी भी मृत्यु और कालके भी पुण्यकर्मोके अवसरपर शरणमें आया है; अतः
- **Translation**: 

---

