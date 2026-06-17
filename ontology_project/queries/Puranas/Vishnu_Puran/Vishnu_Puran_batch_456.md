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

### Verse 1 (Vishnu Puran 0.9101)
- **Original**: कजाज फऔै
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9102)
- **Original**: इे18 अ्रीविष्णुपुराण चौथा अध्याय बसुदेख-देवकीका कारागारसे मोक्ष शपराशर उकाच मां हन्तुममरैर्यज्न: कृतः किल दुरात्मभिः । मद्ठीर्यतापितान्वीरों न त्वेतान्गणयाम्यहम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9103)
- **Original**: 3 किमिन्रेणाल्पवीर्येण कि हरेणैकचारिणा । हरिणा वापि कि साध्यं छिद्रेघ्रुस॒ुरघातिना
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9104)
- **Original**: 4 किमादित्यै: कि वसुभिरल्पवीवें: किमप्रिभि: । कि वान्यैरमरै: सर्वैर्मद्राहुअलनिर्जिते:
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9105)
- **Original**: 5 कि न दृष्टोईमरपतिर्मया संयुगमेत्य सः । पृष्ठलेव बहन्बाणानपागच्छन्न॒ वक्षसा
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9106)
- **Original**: 6 मद्राष्ट्रे वारिता वृष्टियंदा शक्रेण कि तदा । मद्गाणभिन्नैर्जलदैर्नापो मुक्ता यथेप्सिता:
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9107)
- **Original**: 7 किमुर्व्यामतबनीपाला. मद्महुबलभीरव: । न सर्वे सन्नति याता जरासन्धमृते गुरुप्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9108)
- **Original**: 8 अपरेषु ममावज्ञा जायते दैत्यपुड्डवा: । हास्यं॑ मे जायते वीरास्तेषु यत्रपरेघ्षपि
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9109)
- **Original**: 9 तथापि खलु दुष्टानां तेषामप्यध्रिक॑ मया। अपकाराय दैत्यपेद्रा यतनीय॑ दुरात्मनाम्‌
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9110)
- **Original**: 10 तो यश्ञस्विन: केचित्पृथिव्यां ये च याजका: । कार्बो देवापकाराय तेषां सर्तवात्मना बधः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9111)
- **Original**: 119 अीपराशरजी _ बोले--तब कंसने . खिन्न- चित्तसे प्ररम्ब और केशी आदि समस्त मुख्य-मुख्य असुरोको बुल्मकर कहा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9112)
- **Original**: कंस कोलछा--हे प्ररुम्ब ! हे महाबाहो केशिन्‌ ! हे धेनुक ! हे पूतने ! तथा हे अरिष्ट आदि अन्य असुरगण ! मेण बचन खुनो--
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9113)
- **Original**: यह यात प्रसिद्ध हो रही है कि दुरात्मा देवताओंने मेरे मारनेके लिये कोई यज्ञ किया है; किन्तु मैं वीर पुरुष अपने बीर्यसे सतावे हुए इन ल्मेगॉकों कुछ भी नहीं गिनता हूँ
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9114)
- **Original**: अल्पवीर्य इन्द्र, अकेले घूमनेबाले महादेव अथवा छिद्र (असावधानीका समय) ढूँढ़कर दैत्योंका वध करनेवाले विष्णुसे उनका क्‍या सत्र्य सिद्ध हो सकता है ?
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9115)
- **Original**: मेंरे बाहुबलसे दलित आदिस्‍्यों, अल्पबीर्य वसुगणों, अग्रियों अथवा अन्य समस्त देखताओंसे भी मेरा कया अनिष्ट हो सकता है ?
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9116)
- **Original**: आपलोगोंने क्‍या देखा नहीं था कि मेरे साथ युद्धभूमिमें आकर देवग़ज इन्द्र, वक्षःस्थलमें नहों, अपनी पीठपर बाणोंकी बौछार सहता हुआ भाग गया था
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9117)
- **Original**: जिस समय इन्द्रने गेरे एज्यमें बर्षाका होना बन्द कर दिया था उस समय क्‍या मेघोंने मेरे काणोंसे बिंघकर हो यथेष्ट जल नहीं बरसाया ?
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9118)
- **Original**: हमारे गुरु (श्वशुर) जरासन्धको छोड़कर क्या पृथियीफे और सभी नृपतिगण मेंरे बाहुबलसे भयभीत होकर मेरे सामने सिर नहों झुकाते ?
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9119)
- **Original**: हे दैत्यश्रेष्णण ! देवताओकि प्रति मेरे चित्तमें अजज्जञा होती है और हे वीरगण ! उन्हें अपने (मेरे) वधका यल्र करते देखकर तो मुझे हैसी आती है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9120)
- **Original**: तथापि हे दैल्पेन्द्रों! उन दुष्ट और दुरात्पाओऑके अपकारके लिये मुझे और भी अधिक प्रयल करना चाहिये
- **Translation**: 

---

