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

### Verse 1 (Vishnu Puran 0.2621)
- **Original**: 22 बद्धा समुद्रे यत्क्षिप्तो यश्चितो5स्मि शिलोश्येः । अन्यानि चाप्यसाधूनि यानि पित्रा कृतानि मे
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2622)
- **Original**: 23 त्वयि भक्तिमतो द्वेषाद्घ तत्सम्भवं च यत्‌ । त्वग्रसादात्मभो सह्स्तेन मुच्येत मे पिता
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2623)
- **Original**: 24 श्रीमगवानुकाच प्रह्हद सर्वमेतत्ते मत्मसादाद्धविष्यति अन्यध्व ते वर दष्मि ब्रियतामसुरात्मज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2624)
- **Original**: समस्त विश्व उत्पन्न हुआ है; उन पुरुषोत्तम भगवानक़ों नमस्कार है
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2625)
- **Original**: अ्रीपराशस्जी बोले---उनके इस प्रकार तन्‍्मयता- पूर्वक स्तुति करनेपर पोताम्बरधारो देवाधिदेव भगवान्‌ हरि प्रकट हुए
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2626)
- **Original**: हे द्विज ! उन्हें सहसा प्रकट हुए देख ने खड़े हो गये और गद्गद वाणीसे 'विष्णुभगवानको नमस्कार है! तिष्णुभगवानको नमस्कार है!' ऐसा आएमबार कहने छूंगे
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2627)
- **Original**: अ्रह्ादजी बोले--हे . शरणागत-दुःखहारी श्रीकेशवदेव ! प्रसन्न होइये। हे अच्यूत ! अपने पुण्य- दर्शनोंसे मुझे फिर भी पचित्र कीजिये
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2628)
- **Original**: श्रीभगबान्‌ बोले--हे प्रह्मद
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2629)
- **Original**: मैं तेरी अनन्यभक्तिसे अति प्रसन्न हूँ; तुझे जिस वरकी इच्छा हो गाँगे छे
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2630)
- **Original**: च्रह्मादजी खोस्के--हे नाथ ! सहस्तरों योनियोंमेंसे मै जिस-जिसमें भी जाऊँ उसी-उसीमें, हे अच्यूत ! आपमें मेरे सर्वदा अक्षुण्ण भक्ति रहे।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2631)
- **Original**: अनिबेकी पुरुषोंकी विषयॉमें जैसी अविचल प्रीति होती है वैसी ही आपका स्मरण करते हुए मेरे हृदयसे कभी दूर नहो
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2632)
- **Original**: श्रीभगवान खोस्ठे--हे प्रह्माद ! मुझमें तो तेरी भक्ति है ही और आगे भी ऐसी ही रहेगी; किन्तु इसके अतिरिक्त भी तुझे और जिस तरकी इच्छा हो मुझसे माँग ले
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2633)
- **Original**: प्रह्मादजी खोले--ते देव ! आपकी स्तुतिमें प्रवृत् होनेसे मेरे पिताके चिक्तमें मेरे प्रति जो द्वेष हुआ है उन्हें डससे जो पाप लगा है बह नष्ट हो जाय
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2634)
- **Original**: इसके अतिरिक्त [ उनकी आज्ञासे ] मेरे शारीरपर जो झाख्नाघात किये गये--मुझे अग्निसमूहमें डाल गया, संपॉसे कटवाया गया, भोजनमें जिष दिया गया; बाँधकर समुद्रमें डाल गया, शिलाओंसे दबाया गया तथा और भी जो-जो दुर्व्यवहार पिताजीने मेरे साथ किये हैं, ये सब आपमें भक्ति रखनेवाले पुरुषके प्रति ट्रेष होनेसे, उन्हें उनके कारण जो पाप लगा है, हे प्रभो ! आपकी कृपासे मेरे पिता उससे शीघ्र ही मुक्त हो जायै
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2635)
- **Original**: 22--24
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2636)
- **Original**: । श्रीभगबान बोले--हे प्रह्ाद ! मेरो क़पासे तुम्हारी ये सब इच्छ्आएँ पूर्ण होंगी। हे असुरकुमार ! मैं तुमको एक यर और भी देता हूँ, तुम्हें जो इच्छा हो माँग लो
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2637)
- **Original**: आ* 20 ] प्रथम ऑक्ष 98 प्रह्मद उकच कृतकृत्योउस्पि भगवन्वरेणानेन यत्त्वयि । भवित्री त्वत्मसादेन भक्तिरव्यभिचारिणी
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2638)
- **Original**: 26 धर्मार्थकामैः कि तस्थ मुक्तिस्तस्य करे स्थिता । समस्तजगतां पूले यस्य भक्ति: स्थिरा त्वयि
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2639)
- **Original**: 27 श्रीभगवात्याच यथा ते निश्चलं चेतो मयि भक्तिसमन्वितम्‌। तथा लव मठ्रसादेन निर्वा्ण परमाप्स्यसि
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2640)
- **Original**: 28 श्रीपएाश्चर उवाच इत्युक्त्वान्तर्दधे विष्णुस्तस्य मैत्रेय पश्यतः । स चापि पुनरागम्य बबन्दे चरणौ पितु:
- **Translation**: 

---

