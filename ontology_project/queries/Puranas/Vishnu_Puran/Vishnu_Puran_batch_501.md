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

### Verse 1 (Vishnu Puran 0.10001)
- **Original**: वह अपने खुर्योसे पृथिवीतलज्ये खोंदता, ग्रीबाके बालोंसे बादत्मरेंको छिन्न-भिन्न करता तथा वेगसे चन्द्रमा और सूर्यके मार्गकों भी पार करता गोपोंकी ओर दौड़ा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10002)
- **Original**: उस अश्वरूप दैत्यके हिनहिनानेके शब्दसे भयभोत होकर समस्त गोप और गोपियाँ श्रीगोविन्दकी आरणमें आये 3
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10003)
- **Original**: तब उनके आरहि-त्राहि शब्दकों सुनकर भगवान्‌ कृष्णचन्द्र सजल मेघकी गर्जनाके समान गम्मीर वाणीसे बोले--
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10004)
- **Original**: “हे गोपालूगण ! आपत्प्रेग केशौ (केडाघारी अश्व) से न डरें, आप तो गोप जातिके हैं, फिर इस प्रकार भयभीत होकर आप अपने वीरोचित पुरुषार्थका ल्प्रेप क्यों करते हैं 7
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10005)
- **Original**: यह अल्पवीर्य, हिनहिनानेसे आत्कू फैल्त्नेवाला और चाचनेवात्म दुष्ट अश्व जिसपर राझसगण बलपूर्बक चढ़ा करते हैं, आपलोगोंका क्या बिगाड़ सकता है ?'
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10006)
- **Original**: [ इस प्रकार गोपोंकों भैर्य बैधाकर ले केशीसे कहने लऊगें-- ] “अरे दुष्ट ! इधर आ, पिनाकधारी वीरभद्वने जिस प्रकार पूृषाके दाँत उखाड़े थे उसी प्रकार मैं कृष्ण तेरे सुखसे सारे दाँत गिर दुँगा''
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10007)
- **Original**: ऐसा कहकर श्रीगोविन्द उछलकर केशोके सामने आये और वह अश्वरूपधारी दैल्य भी मुँह स्वोलकर उनकी ओर दौड़ा
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10008)
- **Original**: तब जनार्दनने अपनी बाँह फैलाकर उस अश्वरूपधारी दुष्ट दैत्यके मुखमें डाल दी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10009)
- **Original**: केशीके मुख॒में घुसी हुई भगवान कणाकी बाहुसे टकराकर उसके समस्त दाँत शुत्र मेघखण्डोंके समान टूटकर याहर गिर पड़े
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10010)
- **Original**: हे द्विज ! उत्पत्तिके समयसे ही उपेक्षा की गयो व्याधि जिस प्रकार नाश करनेके लिये बढ़ने लगती है उसी प्रकार केशीके देहमें प्रविष्ट हुई कष्णचद्धकी भुजा बढ़ने छूगी
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10011)
- **Original**: अक्षयें ओठॉके फट जानेसे वह फेनसहित रूधिर समन करने लगा और उसकी आँखें स्नायुबन्धनके ढौले हो जानेसे फूट गयीं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10012)
- **Original**: तब बह मल-मत्र जोड़ता हुआ पृथिवीपर पैर पटकने रूगा, उसकवा दारीर
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10013)
- **Original**: 352 श्रीविष्णुपुराण [ आ* 16 व्यादितास्यमहास्थस्सोडसुरः: कृष्णबाहुना । निपातितो द्विधा भूमो वैद्युतेन यथा द्ुप:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10014)
- **Original**: 14 ट्विपादे पृष्ठपुच्छार्े भ्रवणेकाक्षिनासिके । केशिनस्ते द्विधाभूते शकले द्वे विरेजतु:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10015)
- **Original**: 15 हत्वा तु केशिन कृष्णों गोपालैर्सुदितैर्वृत: । अनायस्ततनुस्स्वस्थो हसंस्तत्रैव तस्थिवान्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10016)
- **Original**: 16 ततो गोष्यश्ष गोपाश्ष हते केशिनि विस्मिता: । तुष्टवुः पुण्डरीकाक्षमनुरागमनोरमस्‌
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10017)
- **Original**: 17 अथाहात्तहितो विष्र नारदों जलदे स्थित: । केशिन॑ निहत॑ दृष्ठा हर्षनिर्भरमानस:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10018)
- **Original**: 18 साथु साथु जगन्नाथ लीलयैव यदच्युत निहतो5यं त्वया केशी छ्लेश्दस्त्रिदिवोकसाम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10019)
- **Original**: 19 युद्धोत्सुको5हमत्यर्थ नरवाजिमहाहवम्‌ । अभूतपूर्बपन्यत्र ड्रष्ट स्वर्गादिहागत:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10020)
- **Original**: 20 कर्माण्यत्रावतारे ते कृतानि मधुसूदन । यानि तैर्विस्मितं चेतस्तोषसेतेन मे गतम्‌
- **Translation**: 

---

