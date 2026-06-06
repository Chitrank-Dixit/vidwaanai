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

### Verse 1 (Vaivtpuran 12.746)
- **Original**: चाहती, इन्द्रपदकी इच्छा नहीं रखती और मोक्षके मैं जगत्से बाहर नहीं हूँ। प्रभो! आप ही जगत्‌के
- **Translation**: 

---

### Verse 2 (Vaivtpuran 12.747)
- **Original**: मार्गमें भी मेरी रुचि नहीं है; अतः आप मेरें पालक हैं। फिर मेरा पालन क्यों नहीं कर रहे
- **Translation**: 

---

### Verse 3 (Vaivtpuran 12.748)
- **Original**: इन श्रेष्ठ प्राणवल्लभको ही मुझे लौटा दें; क्योंकि हैं! 'यह पति है और मैं इसको स्त्री हूँ!। इस
- **Translation**: 

---

### Verse 4 (Vaivtpuran 12.749)
- **Original**: ये मेरे लिये धर्म, अर्थ, काम और मोक्ष-चारों प्रकार जो 'इृदम्‌' और “मम' का भाव उत्पन्न
- **Translation**: 

---

### Verse 5 (Vaivtpuran 12.750)
- **Original**: पुरुषार्थोकी प्राप्ति करानेवाले श्रेष्ठ देवता हैं।
- **Translation**: 

---

### Verse 6 (Vaivtpuran 12.751)
- **Original**: » भ्रह्मखण्ड + 37 &4888#&
- **Translation**: 

---

### Verse 7 (Vaivtpuran 12.752)
- **Original**: & 894 844 944 4 445 444 44 54444 4 165 4546 4 44 4 शक ऋ 44 कक 44% 44 4 4 44% 5 4 4 4 ऋ 54 4 64 55 5 55% 5 जगदीश्वर! पृथ्वीपर जितनी भी स्त्री-जातियाँ हैं,
- **Translation**: 

---

### Verse 8 (Vaivtpuran 12.753)
- **Original**: उद्धासित करती थी। पतिसेवारूप महान्‌ उनमेंसे किसीको भी विधाताने इन गन्धर्वकुमारके
- **Translation**: 

---

### Verse 9 (Vaivtpuran 12.754)
- **Original**: धर्मका अनुष्ठान करके चिरकालसे संचित समान गुणवान्‌ पति नहीं दिया है। किये हुए तेजसे अग्रिकी उत्तम एवं प्रज्वलित इसके अनन्तर मालावती अपने स्वामीके
- **Translation**: 

---

### Verse 10 (Vaivtpuran 12.755)
- **Original**: शिखा-सी उद्दीपसत हो रही थी। पतिके शवको गुणोंका बखान करने लगी और अभन्तमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 12.756)
- **Original**: छातीसे लगाकर योगासन लगाये बैठी थी सहसा कुपित हो नारायण, ब्रह्मा, महादेव
- **Translation**: 

---

### Verse 12 (Vaivtpuran 12.757)
- **Original**: और स्वामीकी सुरम्य वीणाको दाहिने हाथमें तथा धर्म आदि समस्त देवताओंको सम्बोधित
- **Translation**: 

---

### Verse 13 (Vaivtpuran 12.758)
- **Original**: लिये हुए थी। प्राणवल्लभके प्रति भक्ति तथा करके उन्हें शाप देनेको उद्यत हो गयी। तब
- **Translation**: 

---

### Verse 14 (Vaivtpuran 12.759)
- **Original**: स्नेहोके कारण योगमुद्रापूर्वक्क तर्जी और ब्रह्मा आदि देवताओंने क्षीरसागरके तटपर
- **Translation**: 

---

### Verse 15 (Vaivtpuran 12.760)
- **Original**: अद्भुष्ट अंगुलियोंके अग्रभागसे शुद्ध स्फटिक जाकर भगवान्‌ विष्णुकी शरण ली और
- **Translation**: 

---

### Verse 16 (Vaivtpuran 12.761)
- **Original**: मणिकी माला धारण किये थी। मनोहर मालाबतीके भीषण शापसे बचानेकी उनसे
- **Translation**: 

---

### Verse 17 (Vaivtpuran 12.762)
- **Original**: चम्पाकी-सी अड्भ-कान्ति, बिम्बफलके सदृश प्रार्था की। देवताओंके प्रार्थना कर चुकनेपर 4 2 आकाशबाणी हुई--'देबताओ! अब तुम लोग जाओ। यज्ञके मूल हैं भगवान्‌ विष्णु, बे ही ब्राह्मणका रूप धारण करके मालावतीको शान्त करने तथा तुमलोगोंको शापके संकटसे बचानेके लिये जायाँगे।' आकाशवाणीका यह कथन सुनकर सब देवताओंका हृदय प्रसन्नतासे खिल उठा। वे सब-के-सब उत्कण्ठित हो कौशिकीके तटपर
- **Translation**: 

---

### Verse 18 (Vaivtpuran 12.763)
- **Original**: 34% के “ मालावतीके स्थानमें गये। वहाँ पहुँचकर
- **Translation**: 

---

### Verse 19 (Vaivtpuran 12.764)
- **Original**: अरुण ओष्ठ और गलेमें रज्ञोंकी माला शोभा देबताओंने उस सती मालाबती देवीको देखा।
- **Translation**: 

---

### Verse 20 (Vaivtpuran 12.765)
- **Original**: पाती थी। वह सुन्दरी सोलह वर्षकौ-सी वह रत्नरोंके सारभूत इन्द्रनील आदि मणियोंके
- **Translation**: 

---

