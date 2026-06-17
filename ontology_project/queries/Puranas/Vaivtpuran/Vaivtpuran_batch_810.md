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

### Verse 1 (Vaivtpuran 543.14514)
- **Original**: पुनः उतने ही समयतक तपस्या करके श्रीहरिका जिनका अन्त नहीं जानते हैं, देवता और संत
- **Translation**: 

---

### Verse 2 (Vaivtpuran 543.14515)
- **Original**: दर्शन और वरदान पाया। उद्धव! ऐसे परमेश्वरको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 543.14516)
- **Original**: 630 + संक्षिप्त ब्रह्मवैवर्तपुराण « 54####### ## ##$ ## $ # % $ 4 5 $ $ $ $ 5 5 5 4 5 $ ह 4 $ 5 $ $ 5 $ 5 $ $ ## # 4 /# 6 # 588 4 ##8# 4 # 884 /88# 44684 58 मैं आज अपनी आँखोंसे देखूँगा। पूर्वकालमें
- **Translation**: 

---

### Verse 4 (Vaivtpuran 543.14517)
- **Original**: एक निमेषमें हो जाता है, उन परमात्माकों आज भगवान्‌ शंकरने ब्रह्माजीकी आयुपर्यन्त तप
- **Translation**: 

---

### Verse 5 (Vaivtpuran 543.14518)
- **Original**: मैं प्रत्यक्ष देखूँगा। भाई उद्धव! जैसे भूतलके किया। तब ज्योतिर्मण्डलके बीच गोलोकमें
- **Translation**: 

---

### Verse 6 (Vaivtpuran 543.14519)
- **Original**: धूलि-कणोंकी गणना नहीं हो सकती, उसी प्रकार परमात्मा श्रीकृष्णके उन्हें दर्शन हुए। वे श्रीकृष्ण
- **Translation**: 

---

### Verse 7 (Vaivtpuran 543.14520)
- **Original**: ब्रद्माओं तथा ब्रह्माण्डोंकी गणना भी असम्भव सर्वतत्त्व-स्वरूप और सम्पूर्ण सिद्धियोंसे सम्पन्न
- **Translation**: 

---

### Verse 8 (Vaivtpuran 543.14521)
- **Original**: है। उन अखिल ब्रह्माण्डोंके आधार हैं महाविराट्‌, हैं। वे सबके अपने तथा सर्वश्रेष्ठ परमतत्त्व हैं।
- **Translation**: 

---

### Verse 9 (Vaivtpuran 543.14522)
- **Original**: जो श्रीकृष्णके षोडशांशमात्र हैं। प्रत्येक ब्रह्माण्डमें भगवान्‌ शिवने उनके चरणारविन्दोंकी परम
- **Translation**: 

---

### Verse 10 (Vaivtpuran 543.14523)
- **Original**: ब्रह्मा, विष्णु और शिव आदि देवता, मुनि, मनु, निर्मल भक्ति पायी। उद्धव! जिन भक्तवत्सलने
- **Translation**: 

---

### Verse 11 (Vaivtpuran 543.14524)
- **Original**: सिद्ध तथा मानव आदि चराचर प्राणी वास करते अपने भक्त शिवकों अपने समान ही बना दिया,
- **Translation**: 

---

### Verse 12 (Vaivtpuran 543.14525)
- **Original**: हैं। ब्रह्माण्डोंके आधारभूत वे महाविराट्‌ भी, ऐसे प्रभावशाली उन परमेश्वरके आज मैं दर्शन जिनका सोलहवाँ अंश हैं और जिनकी लीलामात्रसे करूँगा। जितने समयमें सहस्तर इन्द्रोंका पतन हो
- **Translation**: 

---

### Verse 13 (Vaivtpuran 543.14526)
- **Original**: आविर्भूत एवं तिरोभूत होते हैं; ऐसे सर्वशासक जाता है, उतने कालतक निराहार रहकर कृशोदर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 543.14527)
- **Original**: परमेश्वरके आज मैं दर्शन करूँगा। हुए भगवान्‌ अनन्तने उन परमात्माकी प्रसन्नताके ऐसा कहकर अक्रूरजी प्रेमावेशसे मूर्च्छित लिये भक्तिभावसे तपस्या की। तब उन्होंने उन
- **Translation**: 

---

### Verse 15 (Vaivtpuran 543.14528)
- **Original**: हो गये। उनका अड्भ-अड्ड पुलकित हो उठा और अनन्त देवको अपने समान ज्ञान प्रदान किया।
- **Translation**: 

---

### Verse 16 (Vaivtpuran 543.14529)
- **Original**: वे नेत्रोंसे आँसू बहाते हुए भगवच्चरणारविन्दोंका उद्धव! उन्हीं परमेश्ररके आज मैं दर्शन करूँगा।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 543.14530)
- **Original**: ध्यान करने लगे। उनका हृदय भक्तिसे भर गया। उद्धवजी! अट्टाईस इन्द्रोंका पतन हो जानेपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 543.14531)
- **Original**: वे परमात्मा श्रीकृष्फे चरणकमलका स्मरण ब्रह्माजीका एक दिन-रात होता है। इसी क्रमसे
- **Translation**: 

---

### Verse 19 (Vaivtpuran 543.14532)
- **Original**: करते हुए भावनासे ही उनकी परिक्रमा करने तोस दिनोंका मास और बारह मासोंका वर्ष
- **Translation**: 

---

### Verse 20 (Vaivtpuran 543.14533)
- **Original**: लगे। उद्धवने अक्रूरकों हृदयसे लगा लिया और मानकर सौ वर्ष पूर्ण होनेपर ब्रह्माजीकी आयु
- **Translation**: 

---

