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

### Verse 1 (Markende Puran 0.2901)
- **Original**: फिर तो ऋ्रोथयें भरी हुई दैत्योंकों यदि इस समव असनज्ञतापुर्वक मेंरे स्वासोके समीप विशाल सेना और अम्ब्रिकानें एक-दूसरेपर तोंखे नहीँ लेगी तो मेँ बलपूर्वक झ्लॉटा पकड़कर
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2902)
- **Original**: सायकों, शक्तियों तथा फ़रस्तोंकों वर्षा आरम्भ चसौटते हुए पुझे ले अल्ुगा!
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2903)
- **Original**: इतनेमें ही देवौका थाहन सिंह क्रोधमें देजयुकव #20+4 भरकर भर्वंकर गर्जना करके गर्दतके- बालोंको दैत्येश्वरेण प्रह्चेतो बलवान्‌ बलसंदृतः। 'हैलाता हुआ असुरॉकी सेनामें कूद पड़ा
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2904)
- **Original**: बल्लान्रयसि पामेवं ततेः कि ते करोम्यहम्‌
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2905)
- **Original**: उसने कुछ दैत्योंकों प॑जॉंकौ मारसे, क्रितनोंको देवी बोलीं--
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2906)
- **Original**: तुप्दें दैत्योके राजाने अपने जबड़ोंसे और कितने हो महादेत्यॉकों पटककर भेजा है, तुम स्वयं भी बलकान्‌ हो और तुम्हे , ओठकी दाढ़ोंसे घायल करके मार डाला
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2907)
- **Original**: साथ बिशाल सेना भी है; ऐसी दशापें यदि मुझे
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2908)
- **Original**: उस समिंहने अपने नखोंसे कितनोंके पेट फाड़ बलपृव्ंक ले चलोगे तो मैं तुप्हारा बचा कर 75 448 7 सकती हूँ
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2909)
- **Original**: ऋषित्यव #( 24 इत्चुक्त: सो5भ्यथावत्तापसुरो धूप्नलोचनः
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2910)
- **Original**: 4 दुंकारेणैत्र त॑ भस्म सा चक्कारास्बिका ततः
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2911)
- **Original**: 55.2] अथ कुद्ध॑ पहासैन्यमसुराणा तथाम्बिका।
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2912)
- **Original**: खबर्ष स्त्रयकेंस्तीद्णीस्तथा शक्तिपरश्चओ:
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2913)
- **Original**: त्रत्तों श्ुतसट: कोपात्कृत्वा नार्द सुभरत्म्‌। पप्रातासुरसेनायां सिंहों देख्या: स्ववाहनः
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2914)
- **Original**: कांशित्‌ करप्रह्मेण दैत्यानास्पेन चापरानू। चार्थरेणान्यान्‌ स जधानगहासुरान्‌
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2915)
- **Original**: केषांसिए्पाटबामास नर: कोष्ठानि केसरी । त्तथा तत्प्रहारेण शिरांसि कृतवान्‌ पृथक
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2916)
- **Original**: विच्छिन्नग्राहुशिस्स: कुतास्तेन तथशापरे। पषौं चर रुछिरं कोझ्लादन्यैपां धुतकेसर:
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2917)
- **Original**: 2 2 आर हि, 8 :4:4-
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2918)
- **Original**: क्षणेत तदबलं॑' सर्व क्षय नीत॑ महात्पना। डाले और थप्पड़ मारकर कितनोंके सिर धड़रे तेन केसरिणा देव्वा वाहमेनातिकोपिना
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2919)
- **Original**: अलग कर दिये
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2920)
- **Original**: कितनोंकी भुजाएँ और ऋषि कहते हैं --
- **Translation**: 

---

