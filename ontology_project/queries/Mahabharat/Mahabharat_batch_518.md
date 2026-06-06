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

### Verse 1 (Mahabharat 0.5171)
- **Original**: “बहुत अच्छा भगवन्‌ ! ऐसा ही करूँगा' यों कहकर
- **Translation**: 

---

### Verse 2 (Mahabharat 0.5171)
- **Original**: “बहुत अच्छा भगवन्‌ ! ऐसा ही करूँगा' यों कहकर
- **Translation**: 

---

### Verse 3 (Mahabharat 0.5172)
- **Original**: श्रीकृष्णका सम्मान किया और झीप्र ही उत्तम बाणोंसे कर्णको बींधना आरम्भ किया। उन्होंने “वत्सदन्त' नामवाले
- **Translation**: 

---

### Verse 4 (Mahabharat 0.5172)
- **Original**: श्रीकृष्णका सम्मान किया और झीप्र ही उत्तम बाणोंसे कर्णको बींधना आरम्भ किया। उन्होंने “वत्सदन्त' नामवाले
- **Translation**: 

---

### Verse 5 (Mahabharat 0.5173)
- **Original**: सायकोंसे कर्णको उसके रथ और घोड़ोंसहित ढक दिया
- **Translation**: 

---

### Verse 6 (Mahabharat 0.5173)
- **Original**: सायकोंसे कर्णको उसके रथ और घोड़ोंसहित ढक दिया
- **Translation**: 

---

### Verse 7 (Mahabharat 0.5174)
- **Original**: और पूरी झक्ति लगाकर चारों दिशाओंको बाणोंसे
- **Translation**: 

---

### Verse 8 (Mahabharat 0.5174)
- **Original**: और पूरी झक्ति लगाकर चारों दिशाओंको बाणोंसे
- **Translation**: 

---

### Verse 9 (Mahabharat 0.5175)
- **Original**: आच्छादित कर दिया। । तदनन्तर, कर्णकों जब चेत हुआ तो उसने धैर्य धारण करके अर्जुनको दस और श्रीकृष्णको छः बाणोंसे बींध
- **Translation**: 

---

### Verse 10 (Mahabharat 0.5175)
- **Original**: आच्छादित कर दिया। । तदनन्तर, कर्णकों जब चेत हुआ तो उसने धैर्य धारण करके अर्जुनको दस और श्रीकृष्णको छः बाणोंसे बींध
- **Translation**: 

---

### Verse 11 (Mahabharat 0.5176)
- **Original**: डाल्मा। अब अर्जुनने कर्णपर एक भर्यंकर बाण छोड़नेका
- **Translation**: 

---

### Verse 12 (Mahabharat 0.5176)
- **Original**: डाल्मा। अब अर्जुनने कर्णपर एक भर्यंकर बाण छोड़नेका
- **Translation**: 

---

### Verse 13 (Mahabharat 0.5177)
- **Original**: विचार किया। इधर, उसके वधकां समय भी आ पहुँचा
- **Translation**: 

---

### Verse 14 (Mahabharat 0.5177)
- **Original**: विचार किया। इधर, उसके वधकां समय भी आ पहुँचा
- **Translation**: 

---

### Verse 15 (Mahabharat 0.5178)
- **Original**: था। उस समय कालने अदृश्य रहकर कर्णको ब्राह्मणके
- **Translation**: 

---

### Verse 16 (Mahabharat 0.5178)
- **Original**: था। उस समय कालने अदृश्य रहकर कर्णको ब्राह्मणके
- **Translation**: 

---

### Verse 17 (Mahabharat 0.5179)
- **Original**: कोपवश्ष दिये हुए झापकी याद दिला दी और उसके वधकी
- **Translation**: 

---

### Verse 18 (Mahabharat 0.5179)
- **Original**: कोपवश्ष दिये हुए झापकी याद दिला दी और उसके वधकी
- **Translation**: 

---

### Verse 19 (Mahabharat 0.5180)
- **Original**: लोग सदा कहा करते थे कि धर्म अवश्य ही मनुष्यकी रक्षा करता है। मैं भी झासत्रमें जैसा सुना गया है और जैसी अपनी शक्ति है, उसके अनुसार धर्मपालनके लिये सदा ही प्रयत्न करता रहा हूँ। किंतु आज वह भी मुझे मार ही रहा है, बचाता नहीं। इसलिये मेरी समझमें तो यही बात आती है कि धर्म भी अपने भक्तोंकी सदा रक्षा नहीं करता।' जब कर्ण ये बातें कह रहा था, उस समय उसके घोड़े और सारधि लड़खड़ा रहे थे। वह स्वयं भी अर्जुनके बाणोंकी मारसे विचल्ित हो उठा था। मर्मस्थानोंमें चोट लूगनेसे वह झिथिल हो गया था, काम करनेकी शक्ति नहीं रह गयी थी। अतः रह-रहकर धर्मकी निन्‍्दा ही करता था। इसके बाद उसने कृष्णके हाथमें तीन और अर्जुनके सात भयंकर
- **Translation**: 

---

### Verse 20 (Mahabharat 0.5180)
- **Original**: लोग सदा कहा करते थे कि धर्म अवश्य ही मनुष्यकी रक्षा करता है। मैं भी झासत्रमें जैसा सुना गया है और जैसी अपनी शक्ति है, उसके अनुसार धर्मपालनके लिये सदा ही प्रयत्न करता रहा हूँ। किंतु आज वह भी मुझे मार ही रहा है, बचाता नहीं। इसलिये मेरी समझमें तो यही बात आती है कि धर्म भी अपने भक्तोंकी सदा रक्षा नहीं करता।' जब कर्ण ये बातें कह रहा था, उस समय उसके घोड़े और सारधि लड़खड़ा रहे थे। वह स्वयं भी अर्जुनके बाणोंकी मारसे विचल्ित हो उठा था। मर्मस्थानोंमें चोट लूगनेसे वह झिथिल हो गया था, काम करनेकी शक्ति नहीं रह गयी थी। अतः रह-रहकर धर्मकी निन्‍्दा ही करता था। इसके बाद उसने कृष्णके हाथमें तीन और अर्जुनके सात भयंकर
- **Translation**: 

---

