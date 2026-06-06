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

### Verse 1 (Vaivtpuran 39.8279)
- **Original**: + मणपतिखण्ड » 387 4548 %84%8## ऋऋ # 5 5 5 4 5 ऊ कक 5 $ # $ 5 8 %# 2954 95 844 4448 4 4 % 4 4 4 4 4 % ऋ कक % 8 % 8 4 ऊ हक क़ कक कक # कफ गोलोकधाममें भगवान्‌ श्रीकृष्णके दर्शन कराये।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 39.8280)
- **Original**: इधर वह दाँत खूनसे सनकर शब्द करता हुआ उस समय भगवान्‌ रज्नाभरणोंसे विभूषित हो
- **Translation**: 

---

### Verse 3 (Vaivtpuran 39.8281)
- **Original**: भूमिपर गिर पड़ा, मानो गेरुसे युक्त स्फटिकका रत्ननिर्मित सिंहासनपर आसीन थे। राधाजी उनके रा " वक्षःस्थलसे सटी हुई थीं। तेजमें बे करोड़ों सूर्योके समान प्रभाशाली थे। उनके दो भुजाएँ न थीं, हाथमें मुरली शोभा पा रही थी, परम मनोहर
- **Translation**: 

---

### Verse 4 (Vaivtpuran 39.8282)
- **Original**: रूप था और वे मन्द-मन्द मुस्करा रहे थे। इस
- **Translation**: 

---

### Verse 5 (Vaivtpuran 39.8283)
- **Original**: प्रकार श्रीकृष्णके दर्शन कराकर उनसे बारंबार
- **Translation**: 

---

### Verse 6 (Vaivtpuran 39.8284)
- **Original**: प्रणाम कराया। यों सम्पूर्ण पापोंका पूर्णतया नाश
- **Translation**: 

---

### Verse 7 (Vaivtpuran 39.8285)
- **Original**: (% कर देनेवाले इष्टदेव श्रीकृष्णके दर्शन कराकर
- **Translation**: 

---

### Verse 8 (Vaivtpuran 39.8286)
- **Original**: ] गणेशजीने परशुरामके भ्रूणहत्याजनित पापको दूर 4 कर दिया। यों तो पापजनित यातना भोगे बिना
- **Translation**: 

---

### Verse 9 (Vaivtpuran 39.8287)
- **Original**: केक ले नष्ट नहीं होती, किंतु परशुरामको थोड़ी ही भोगनी
- **Translation**: 

---

### Verse 10 (Vaivtpuran 39.8288)
- **Original**: पर्वत धराशायी हो गया हो। विप्रवर! उस महान्‌ पड़ी और सब श्रीकृष्णके दर्शनसे नष्ट हो गयी।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 39.8289)
- **Original**: शब्दसे भयभीत होकर पृथ्वी काँप उठी। सभी क्षणभरके बाद परशुरामकी चेतना लौट आयी
- **Translation**: 

---

### Verse 12 (Vaivtpuran 39.8290)
- **Original**: कैलासवासी प्राणी उसी क्षण डरके मारे मूच्छित॑ और वे वेगपूर्वक भूतलपर गिर पड़े। उस समय
- **Translation**: 

---

### Verse 13 (Vaivtpuran 39.8291)
- **Original**: हो गये। उस समय निद्राके स्वामी जगदीश्वर उनका गणेशद्वारा किया गया स्तम्भन भी दूर हो
- **Translation**: 

---

### Verse 14 (Vaivtpuran 39.8292)
- **Original**: शिवकी निद्रा भंग हो गयी। वे घबराये हुए गया। तब उन्होंने अपने अभीष्टदेव श्रीकृष्ण,
- **Translation**: 

---

### Verse 15 (Vaivtpuran 39.8293)
- **Original**: पार्वतीके साथ अन्तःपुरसे बाहर आये। मुने! उस अपने गुरु जगद्गुरु शम्भु तथा गुरुद्वारा दिये गये
- **Translation**: 

---

### Verse 16 (Vaivtpuran 39.8294)
- **Original**: समय गणेश घायल हो गये थे, उनका दाँत टूट परम दुर्लभ स्तोत्र और कवचका स्मरण किया।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 39.8295)
- **Original**: गया था और मुख रक्तसे सराबोर था। उनका मुने! तदनन्तर परशुरामने अपने अमोघष फरसेको,
- **Translation**: 

---

### Verse 18 (Vaivtpuran 39.8296)
- **Original**: क्रोध शान्त हो गया था और वे लज्जित होकर जिसकी प्रभा ग्रीष्म-ऋतुके मध्याह्कालिक
- **Translation**: 

---

### Verse 19 (Vaivtpuran 39.8297)
- **Original**: मुस्कराते हुए सिर झुकाये हुए थे। उन्हें इस सूर्यकी प्रभासे सौगुनी थी और जो तेजमें शिव-
- **Translation**: 

---

### Verse 20 (Vaivtpuran 39.8298)
- **Original**: दशामें सामने देखकर पार्वतीने शीघ्र ही स्कन्दसे तुल्य था, गणेशपर चला दिया। पिताके उस
- **Translation**: 

---

