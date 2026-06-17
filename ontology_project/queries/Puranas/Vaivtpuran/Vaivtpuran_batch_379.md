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

### Verse 1 (Vaivtpuran 18.1299)
- **Original**: लोकमें सुख भोगता, परम दुर्लभ कोर्ति प्राप्त इस स्तोत्रका श्रवण करता है, बह यदि भार्याहीन
- **Translation**: 

---

### Verse 2 (Vaivtpuran 18.1300)
- **Original**: करता और नाना प्रकारके धर्मका अनुष्ठान करके हो तो अति विनयशील सती-साध्वी सुन्दरी भार्या
- **Translation**: 

---

### Verse 3 (Vaivtpuran 18.1301)
- **Original**: अन्तमें भगवान्‌ शंकरके धामकों जाता है, वहाँ पाता है। जो महान्‌ मूर्ख और खोटी बुद्धिका है,
- **Translation**: 

---

### Verse 4 (Vaivtpuran 18.1302)
- **Original**: श्रेष्ठ पार्षद होकर भगवान्‌ शिवकी सेवा करता है। ऐसा मनुष्य यदि इस स्तोत्रकों एक मासतक (अध्याय 19) 22000 य30000000 गोपपल्नी कलावतीके गर्भसे एक शिशुके रूपमें उपबईणका जन्म, शूद्रयोनिमें उत्पन्न बालक नारदकी जीवनचर्या, नामकी व्युत्पत्ति, उसके द्वारा संतोंकी सेवा, सनत्कुमारद्वारा उसे उपदेशकी प्राप्ति, उसके द्वारा श्रीहरिके स्वरूपका ध्यान, आकाशवाणी तथा उस बालकके देह-त्यागका वर्णन सौति कहते हैं--उपबर्हण गन्धर्व अपनी
- **Translation**: 

---

### Verse 5 (Vaivtpuran 18.1303)
- **Original**: संस्कार करके गन्धर्व उपबर्हणने ब्राह्मणोंको नाना पत्नी मालावतीके साथ तथा अन्य पत्नियोंके साथ
- **Translation**: 

---

### Verse 6 (Vaivtpuran 18.1304)
- **Original**: प्रकारके धन दिये। शौनकजी! फिर अन्तकाल भी निर्जन बनमें आनन्दपूर्वक बिहार करने लगे। आनेपर ब्रह्माजीके शापसे प्राणोंका परित्याग उन्होंने अपनी आयुका शेष काल सानन्द बिताना
- **Translation**: 

---

### Verse 7 (Vaivtpuran 18.1305)
- **Original**: करके उस दिद्वान्‌ गन्धर्वने ब्राह्मणके वीर्य और आरम्भ किया। उपबर्हणके पिता गन्धर्वराज भी
- **Translation**: 

---

### Verse 8 (Vaivtpuran 18.1306)
- **Original**: शुद्राके गर्भसे जन्म ग्रहण किया। सती मालावतीने स्त्री-पुत्रोंके साथ प्रसन्नतापूर्वक रहने लगे। उन्होंने
- **Translation**: 

---

### Verse 9 (Vaivtpuran 18.1307)
- **Original**: मनमें उत्तम संकल्प ले भारतभूमिके पुष्कर तीर्थमें नाना प्रकारके श्रेष्ठ कर्म तथा बड़े-बड़े पुण्य कर्म
- **Translation**: 

---

### Verse 10 (Vaivtpuran 18.1308)
- **Original**: अग्निकुण्डके भीतर अपने प्राणोंका परित्याग कर किये। वे कुबेर-भवनके समान वैभवशाली गृहमें
- **Translation**: 

---

### Verse 11 (Vaivtpuran 18.1309)
- **Original**: दिया। वह साध्वी मनुबंशी राजा सृंजयकी पत्नीसे राजा होकर राजसुखका उपभोग करने लगे।
- **Translation**: 

---

### Verse 12 (Vaivtpuran 18.1310)
- **Original**: उत्पन्न हुई। उसे पूर्वजन्मकी बातोंका स्मरण रहता उन्होंने अपनी सुस्थिरयौवना सुशीला पत्नीके साथ
- **Translation**: 

---

### Verse 13 (Vaivtpuran 18.1311)
- **Original**: था। उस सुन्दरीके मनमें यही संकल्प था कि कुछ कालतक विहार किया। फिर समय आनेपर
- **Translation**: 

---

### Verse 14 (Vaivtpuran 18.1312)
- **Original**: उपबर्हण गन्धर्व मेरे पति हों। गज्जाजीके मनोहर तटपर पत्नीसहित गन्धर्वराज शौनकजीने पूछा--सूतनन्दन! उपबर्हण गन्धर्व प्राणोंका परित्याग करके सानन्द बैकुण्ठधामको
- **Translation**: 

---

### Verse 15 (Vaivtpuran 18.1313)
- **Original**: ब्राह्मणके वीर्य और शुद्र-पत्नीके गर्भसे किस चले गये। वे शैव थे, इसलिये उनपर शिवजीकी
- **Translation**: 

---

### Verse 16 (Vaivtpuran 18.1314)
- **Original**: प्रकार उत्पन्न हुए? यह आप बतानेकी कृपा करें। कृपा हुई तथा उनके पुत्रने श्रीविष्णुकी सेवा की शौनकजीके यों पूछनेपर सूतजीने 'गोपराज थी, इसलिये भगवान्‌ विष्णुकी भी उनपर
- **Translation**: 

---

### Verse 17 (Vaivtpuran 18.1315)
- **Original**: द्रमिलकी पत्नी कलाबतीने मुनिबर काश्यपके कृपादृष्टि हुई। इससे वे वैकुण्ठमें श्रीविष्णुके
- **Translation**: 

---

### Verse 18 (Vaivtpuran 18.1316)
- **Original**: स्खलित शुक्रकों ग्रहण कर लिया था, इससे चतुर्भुजरूपधारी पार्षद हुए। माता-पिताका
- **Translation**: 

---

### Verse 19 (Vaivtpuran 18.1317)
- **Original**: उसको पुत्रकी प्राप्ति हुई थी'-इस प्रकार
- **Translation**: 

---

### Verse 20 (Vaivtpuran 18.1318)
- **Original**: उपबर्हणके जन्मकी कथा सुनाकर कहा कि
- **Translation**: 

---

