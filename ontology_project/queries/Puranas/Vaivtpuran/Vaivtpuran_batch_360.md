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

### Verse 1 (Vaivtpuran 16.3694)
- **Original**: स्‍्वगें मर्त्वे च पाताले वैकुण्ठे मम संनिधी । भवन्तु तुलसोवृक्षा वरा; पुष्पेषु सुन्दरि
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3695)
- **Original**: गोलोके विरजातोरे रासे वुन्दानने भुषि । भाण्डीी चम्पयकवने रम्ये. चन्दनकानने
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3696)
- **Original**: 'म्राधवीकेतकी कुन्दर्माश्चकामालती वने भवन्तु तरवस्तत्र. पुण्यस्थानेषु. पुण्यदा:
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3697)
- **Original**: तुलसीतरुमूले.. च पुण्यदेशे. सुपुण्यदे । अधिष्ठान॑तु॒तीर्थानां सर्वेषां च भविष्यति
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3698)
- **Original**: तत्व. सर्वदेवााां समधिष्ठाममेव. च । तुलसोपत्रपतनप्रास्ये च बरानने
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3699)
- **Original**: स॒ खस्रातः: सर्वतीर्थेषु सर्वयज्ञेप दीक्षित: । तुलसीपत्रतोयेन यो5भिषेक॑ समाचरेत्‌
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3700)
- **Original**: सुधाघटसहस्नेण सा तुष्टिन भवेद्धर। या च॑ तुष्टिभंवेन्रणां. तुलसीपत्रदानत:
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3701)
- **Original**: गवामयुतदानेन यत्फलं. लभते नरः
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3702)
- **Original**: तुलसीपत्रदानेना तत्फलं. लभते . सति
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3703)
- **Original**: तुलसीपत्रतोयं च मृत्युकाले च यो लभेत्‌ । मुच्यते सर्वपापेभ्यो विष्णुलोकं से गच्छति
- **Translation**: 

---

### Verse 11 (Vaivtpuran 17.944)
- **Original**: 8 + संक्षिप्त अहावैयर्तपुराण कु कड़क %
- **Translation**: 

---

### Verse 12 (Vaivtpuran 17.945)
- **Original**: कक % कक $% %#% %% % #% %$% ऋ$%%$%%ऋ$%%$%%%$$%%$%%$%$%$%$%$%%$%%$%$%$%%%$%%%#%% % %% %% % $ # ;# # # # #ऋ ब्राह्मणग-बालकके साथ क्रमशः ब्रह्मा, महादेवजी तथा धर्मकी बातचीत, देवताओंद्वारा श्रीविष्णुकी तथा ब्राह्मणद्वारा भगवान्‌ श्रीकृष्णकी उत्कृष्ट महत्ताका प्रतिपादन सौति कहते हैं--ब्राह्मणफो आया देख
- **Translation**: 

---

### Verse 13 (Vaivtpuran 17.946)
- **Original**: ब्रह्माने यह परम मज़लमय सत्य एवं हितकर देबसमुदाय उठकर खड़ा हो गया था। फिर वहाँ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 17.947)
- **Original**: बात कही। सभामें उन सबकी परस्पर बातचीत हुई। ये
- **Translation**: 

---

### Verse 15 (Vaivtpuran 17.948)
- **Original**: ब्रह्माजी बोले--मेरे पुत्र नारद ही शापवश ब्राह्मणरूपधारी साक्षात्‌ भगवान्‌ विष्णु हैं, यह
- **Translation**: 

---

### Verse 16 (Vaivtpuran 17.949)
- **Original**: उपबर्हण नामक गन्धर्व हुए थे। फिर मेरे ही बात देवताओंकी समझमें नहीं आयी। भगवान्‌
- **Translation**: 

---

### Verse 17 (Vaivtpuran 17.950)
- **Original**: शापसे उन्होंने योगधारणाद्वारा प्राणोंको त्याग विष्णुकी मायासे मोहित होनेके कारण वे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 17.951)
- **Original**: दिया। भूतलपर उपबर्हणकी स्थिति एक लाख पूर्वापरकी सारी बातें भूल गये थे। शौनकजी!
- **Translation**: 

---

### Verse 19 (Vaivtpuran 17.952)
- **Original**: युगतक नियत की गयी थी। इसके बाद वे उस समय ब्राह्मणने सब देवताओंको सम्बोधित
- **Translation**: 

---

### Verse 20 (Vaivtpuran 17.953)
- **Original**: शूद्रयोनिमें पहुँचकर उस शरीरको त्यागनेके बाद करके मधुर बाणीमें वह सत्य बात कही, जो
- **Translation**: 

---

