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

### Verse 1 (Vaivtpuran 8.2745)
- **Original**: मूच्छित-से हो गये। जान पड़ता था, मानो सब श्रीराधाजीकी पूजा की और फिर बे वहाँ
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.2746)
- **Original**: चित्र-विचित्र पुतले हैं। बड़ी कठिनतासे किसी विराजमान हो गये। इतनेमें भगवान्‌ श्रीकृष्णको
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.2747)
- **Original**: प्रकार उन्हें चेत हुआ। उस समय देखा गया संगीत सुनानेवाली देवी सरस्वती हाथमें वीणा
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.2748)
- **Original**: कि समस्त रासमण्डलमें सम्पूर्ण स्थल जलसे लेकर सुन्दर ताल-स्वरके साथ गीत गाने लगीं।
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.2749)
- **Original**: आप्लाबित है। श्रीराधा और श्रीकृष्णका कहीं पता तब ब्रह्माने पसन्न होकर एक सर्वोत्तम र्नसे बना
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.2750)
- **Original**: नहीं है। फिर तो गोप, गोपी, देवता और हार पुरस्कार-रूपमें उन्हें अर्पण किया। शिवसे
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.2751)
- **Original**: ब्राह्मफग--सभी अत्यन्त उच्च स्वर्से विलाप करने उन्हें अखिल ब्रह्माण्डके लिये दुर्लभ एक उत्तम
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.2752)
- **Original**: लगे। उस समय ब्रह्माजी भी वहीं थे। उन्होंने मणि प्राप्त हुई। भगवान्‌ श्रीकृष्णने उन्हें सम्पूर्ण ध्यानके द्वारा भगवान्‌ श्रीकृष्णका पुनीत विचार रल्ॉमें श्रेष्ठ कौस्तुभभणि भेंट की। राधाने अमूल्य समझ लिया। भगवान्‌ श्रीकृष्ण ही श्रीराधाके साथ रल्ञोंसे निर्मित एक अनुपम हार, भगवान्‌ नारायणने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.2753)
- **Original**: जलमय हो गये हैं-यह बात उन्हें भलीभाँति एक सुन्दर पुष्पमाला तथा लक्ष्मीने बहुमूल्य
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.2754)
- **Original**: मालूम हो गयी। तब बे सभी महाभाग देवता रत्रोंके दो कुण्डल सरस्वतीको पुरस्काररूपमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.2755)
- **Original**: परव्रह्म परमात्मा श्रीकृष्णकी स्तुति करने लगे। दिये। विष्णुमाया, ईश्वरी, दुर्गा, नारायणी और
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.2756)
- **Original**: सबने अपनी प्रार्थना सुनायी। ईशाना नामसे विख्यात भगवती मूलप्रकृतिने *विभो! हमारा केवल यही अभीष्ट वर है सरस्वतीके अन्तःकरणमें परम दुर्लभ परमात्मभक्ति
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.2757)
- **Original**: कि आप अपनी श्रीमूर्तिके हमें पुन: दर्शन करा प्रकट की। धर्मने धार्मिक बुद्धि उत्पन्न करनेके
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.2758)
- **Original**: दें।। ठीक उसी समय अति मधुर तथा स्पष्ट साथ ही प्रपञ्लात्मक जगत्‌में उनकी कीर्ति विस्तृत
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.2759)
- **Original**: शब्दोंमें आकाशवाणी हुई। सब लोगोंने उसे की। अग्रिदेवने चिन्मय वस्त्र तथा पवनदेवने
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.2760)
- **Original**: भलीभाँति सुना। आकाशवाणीमें कहा गया--' मैं मणिमय नूपुर सरस्वतीको प्रदान किये। सर्वात्मा श्रीकृष्ण और मेरी स्वरूपाशक्ति राधा--हम इतनेमें ब्रह्मासे प्रेरित होकर भगवान्‌ शंकर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.2761)
- **Original**: दोनोंने ही भक्तोंपर अनुप्रह करनेके लिये यह
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.2762)
- **Original**: जलमय विग्रह धारण कर लिया है। सुरेश्वरो!
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.2763)
- **Original**: निर्माण करूँगा '--यह विचार उनके इृदयमें गूँजने तुम्हें मेरे तथा इन राधाके शरीरसे क्‍या प्रयोजन
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.2764)
- **Original**: लगा। उन्होंने अपना विचार व्यक्त किया कि है? मनु, मुनि, मानव तथा अगणित वैष्णवजन
- **Translation**: 

---

