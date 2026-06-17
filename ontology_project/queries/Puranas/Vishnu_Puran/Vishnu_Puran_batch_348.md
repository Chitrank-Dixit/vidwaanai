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

### Verse 1 (Vishnu Puran 0.6941)
- **Original**: ततो रघुरभवत्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.6942)
- **Original**: . तस्मादप्यजः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.6943)
- **Original**: अजाइशरथ:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.6944)
- **Original**: तस्थापि भगवानब्जनाभों जगत: -स्थित्यर्थमात्मांहेन रामलक्ष्मणभरत- जन्रुम्नरूपेण चतुर्द्धा पुत्रत्वमायासीत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.6945)
- **Original**: तभीसे राजाने ख्ीं-सम्मोग त्याग दिया
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.6946)
- **Original**: पीछे पुत्रहोन राजाके प्रार्थना करनेपर वसिष्ठजोने मदयन्तीके गर्भाधान किया
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.6947)
- **Original**: जब उस गर्भने सात वर्ष व्यतीत प्रहार किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.6948)
- **Original**: इससे उसी समय पुत्र उत्पन्न हुआ और उसका नाम अक््मक हुआ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.6949)
- **Original**: अच्मकके मूलक नामक पूत्र हुआ
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.6950)
- **Original**: जब परशुरामजीड्वारा यह पृथिवीतल क्षत्रियहीन किया जा रहा था उस समय उस (मूलक) की रक्षा वख्नरहीना स्वियोंने खेरकर को थी, इससे उसे नारीकवच भी कहते हैं
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.6951)
- **Original**: मूलकके दद्गार्थ, दद्वारथके इलिविक, इकिविलके विधसह और विश्वसहके ख़ट्वाड़ नामक पुत्र हुआ, जिसने देखासुरसंग्रामें देवताओंके प्रार्थना करनेपर दैल्यॉका वध क्रिया था।
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.6952)
- **Original**: इस प्रकार स्वर्गमें देवताओंका प्रिय करनेसे उनके द्वारा वर माँगनेके ल्थ््यि प्रेरित किये जानेपर उसने कहा---
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.6953)
- **Original**: “यदि मुझे नर ग्रहण करना ही पड़ेगा तों आपलोग मेरी आयु बतत्याइये'
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.6954)
- **Original**: तब देखताओंके यह कहनेपर कि तुम्हारी आयु केबल एक मुहूर्त और रही है वह [ देबताओंके दिये हुए ] एक अनवरुद्धनवि विमानपर बैठकर बड़ो शोघतासे मर्व्यलोकमें आया और कहने छगा--
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.6955)
- **Original**: “ग्रदि मुझे ब्राह्मणोंक्री अपेक्षा कभी अपना आत्मा भो प्रियतर नहीं हुआ, यदि मैने कभी स्वधर्मका उल्त्हुन नहीं किया और सम्पूर्ण देव, मनुष्य, पशु, पक्षी और बृक्षादिमें श्रीअच्युतके अतिरिक्त मेरी अन्य *
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.6956)
- **Original**: दृष्टि नहों हुई तो मै निर्विश्नतापूर्वक उन मुनिजनवन्दित प्रभुकों प्राप्त होऊँ।' ऐसा कहते हुए गजा स्ट्बाडुने सम्पूर्ण देवताओंके गुरु, अकधनीयस्वरूप, सत्तामात्र- शरीर, परमात्मा भगवान्‌ वासुदेयर्में अपना चित्त लूगा दिया और उन्‍्हींमें ल्लैन हो गये
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.6957)
- **Original**: इस विषयमें भी पूर्वकालमें सप्तर्षियोंद्राय कहा हुआ इलोक सुना जाता है। [उसमें कहा है---] 'खट्वाड़नके समान पृथिवीटलमें अन्य कोई भी राजा नहीं होगा, जिसने मुहूर्तमात्र जीवनके रहते ही स्वर्गस्प्रेकसे भूमण्डलमें आकर अपनी बुडिद्वार तोनों लोकोंको सत्यस्वरूप भगवान्‌ वासुदेवमय देखा'
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.6958)
- **Original**: खट्वाड़से दीर्घच्राहु नामक पुत्र हुआ दीर्घजाहसे रघु, रघुसे अज और अजसे दशरथने जन्म लिया
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.6959)
- **Original**: 83--86
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.6960)
- **Original**: दशशरथजीके भगवान्‌ क्मलनाभ जगत्‌की स्थितिके जिये अपने अंशोंसे राम; लक्ष्मण, भरत और शत्रुघ्न
- **Translation**: 

---

