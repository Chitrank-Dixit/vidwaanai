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

### Verse 1 (Vishnu Puran 0.541)
- **Original**: 10 ज्रजास्ता ब्रह्मणा सृष्टाश्ञातुर्वण्यव्यवस्थिता: । सम्बक्ठ्ुद्धासमाचारप्रजणा._ मुनिसत्तम
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.542)
- **Original**: 115 यथेच्छाबासनिरता: सर्वबाधाविवर्जिता: । झुद्धान्तःकरणा: शुद्धाः कर्मानुष्ठाननिर्मलछा:
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.543)
- **Original**: 12 शुद्धे च तासां मनसि झुद्धेउन्तः संस्थिते हरो । झुद्धज्ञानं प्रपश्यन्ति विष्णवाख्य॑ येन तत्पदम्‌
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.544)
- **Original**: 13 ततः कालात्मको बो5सौ स चांश: कथितो हरे: । सपातयत्यघ॑घोरमल्पपल्पाल्पसारबत्‌ । 14 श्रीमैत्रेयजी बोले--हे भगवन्‌ ! आपने जो अर्वाकु-खोता मनुष्योंके पिघयसें कहा ठनकी सृष्टि ग्रह्मजीने किस ग्रकार कौ--यह विस्तारपूर्वक कहिये
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.545)
- **Original**: श्रीप्रजापतिने त्राह्मणादि वर्णकों जिन-जिन गुणोंसे युक्त और जिस प्रकार रचा तथा उनके जो-जो कर्तव्य- कर्म निर्धारित किये बह सब जर्णन कीजिये
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.546)
- **Original**: श्रीपराश्रजी चोले--हे ब्विजश्रेष्ट / जगत- रघनाकी इच्छासे युक्त सल्यसंकएप श्रीत्रद्माजीके मुखसे पहले सच्त्यप्रधान प्रजा उत्पन्न हुई
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.547)
- **Original**: तदनच्तर उनके वक्षःस्थल्से रजःप्रज्चान तथा जंभाओँसे रज और तमविशिष्ट सृष्टि हुई
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.548)
- **Original**: हे ट्विजोत्तम ! चरणोंसे कद्याजीगी एक और प्रकास्की प्रजा उत्पन्न की, बह तम प्रधान थी : ये ही सब चारों वर्ण हुए
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.549)
- **Original**: इस प्रक्पर हे द्विजसत्तम ! ब्राह्मण, झत्रिय, बैदय और शूद्व ये चारो क्रमज: बहाजीके मुख, वक्षःस्थछ, जानु और चरणोंसे उत्पन्न हुए
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.550)
- **Original**: हे महाभाग ! ब्रह्मजीने यज्ञानुप्ठानके ल्त्यि ही यज्ञके उत्तम साधनरूप इस सम्पूर्ण चातुर्वर्ण्यकी रचना बी श्री
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.551)
- **Original**: हे घर्मश ! सज्ञसे तृप्त होकर देवागण जछ बरसाकर पग्रजाको तृप्त करते हैं; अतः यज्ञ सर्वधा कल्याणका हेतु है
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.552)
- **Original**: जो मनुष्य सदा स्वधर्मपणयण, सदाचारी, सज्जन और सुमार्गगामी होते हैं उत्हींसे वज्ञका यथायत्‌ अनुष्ठान हो सकता है
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.553)
- **Original**: हे मुने ! [यशके द्वारा) मनुष्य इस मनुष्य-शरीरसे ही स्वर्ग और अपवर्ग प्राप्त कर सकते हैं; तथा और भी जिस स्थानको उन्हें इच्छा हो उसीक्प्रे जा सकते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.554)
- **Original**: है मुनिसत्तम ! श्रह्माजीद्वारा रचों हुई वह चातुर्वर्ण्य-डिभागमें स्थित प्रजा अति श्रद्धायुत्त आचरणवाली, स्वेच्छानुसार रहनेचाली, सम्पूर्ण आाघाऑसे रहित, इाुद्ध अचाःकरणवाली, सत्कुलोत्पन्न और पृष्य कमोंके अनुष्ठानसे परम पवित्र थी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.555)
- **Original**: 615-12
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.556)
- **Original**: उसका चित शुद्ध होनेफे कारण उसमें निरन्तर झुद्धस्वरूम श्रीहरिके विराजमान रहनेसे उन्हें शुद्ध ज्ञान प्राप्त होता था जिससे ले भगवान्‌क्के उस 'व्रिष्णु' गामक परम पटको देख पाते थे
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.557)
- **Original**: फिर (त्रेतायुगके आरम्भमें), हमने तुमसे भगवान्‌के जिस काल गामक अंज्ञका पहले वर्णन किया है,
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.558)
- **Original**: आ*6 ] अश्चवम अंडा 21 अधर्मबीजसमुद्धते तमोलोभसमुद्धवम्‌ बह अति अल्प सारबाले (सुखबाले) तुच्छ और घोर ब्जासु तासु पैत्रेय रागादिकमसाधकम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.559)
- **Original**: (दुःखमय) पापॉफो प्रजायें प्रवुत कर देता है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.560)
- **Original**: हे ततः सा सहजा सिद्धिस्तासों नातीव जायते । रसोल्लासादयश्ान्या: सिद्धबोहछो भवन्ति या:
- **Translation**: 

---

