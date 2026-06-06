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

### Verse 1 (Mahabharat 0.431)
- **Original**: आिपर्य ] सूर्षपुत्री तपतीके साथ राजा संवरणका वियाह 95 बोली । बादलमें बिजलीकी तरह तत्क्षण अन्तर्धान हो गयी।
- **Translation**: 

---

### Verse 2 (Mahabharat 0.431)
- **Original**: आिपर्य ] सूर्षपुत्री तपतीके साथ राजा संवरणका वियाह 95 बोली । बादलमें बिजलीकी तरह तत्क्षण अन्तर्धान हो गयी।
- **Translation**: 

---

### Verse 3 (Mahabharat 0.432)
- **Original**: मुँह करके भगवान्‌ सूर्यकी आसथना करने रगे। उन्होंने राजाने उसे ढैढ़नेकी बड़ी चेष्टा की । अन्तमें असफल होनेपर
- **Translation**: 

---

### Verse 4 (Mahabharat 0.432)
- **Original**: मुँह करके भगवान्‌ सूर्यकी आसथना करने रगे। उन्होंने राजाने उसे ढैढ़नेकी बड़ी चेष्टा की । अन्तमें असफल होनेपर
- **Translation**: 

---

### Verse 5 (Mahabharat 0.433)
- **Original**: घन-हौ-मन अपने पुरोहित महर्षि बसिश्ठका ध्यान किया। विल्मप करते-करते वे निश्चेष्ट हो गये। ठीक बारहवें दिन वसिष्ठ महर्षि आये उन्होंने राजा संबरणके राजा संवरणको बेहोप्न और धरतीपर पड़ा देखकर तपती
- **Translation**: 

---

### Verse 6 (Mahabharat 0.433)
- **Original**: घन-हौ-मन अपने पुरोहित महर्षि बसिश्ठका ध्यान किया। विल्मप करते-करते वे निश्चेष्ट हो गये। ठीक बारहवें दिन वसिष्ठ महर्षि आये उन्होंने राजा संबरणके राजा संवरणको बेहोप्न और धरतीपर पड़ा देखकर तपती
- **Translation**: 

---

### Verse 7 (Mahabharat 0.434)
- **Original**: मंनका सारा हाल जानकर उन्हें आश्वासन दिया और उनके फिर वहाँ आयी और मिठासभरी वाणीसे बोली, 'राजन्‌ !
- **Translation**: 

---

### Verse 8 (Mahabharat 0.434)
- **Original**: मंनका सारा हाल जानकर उन्हें आश्वासन दिया और उनके फिर वहाँ आयी और मिठासभरी वाणीसे बोली, 'राजन्‌ !
- **Translation**: 

---

### Verse 9 (Mahabharat 0.435)
- **Original**: सामने ही भगवान्‌ सूर्यसे मिलनेके लिये चल पड़े। सूर्यके उठिये, उठिये। आप-जैसे सत्युरुवको अचेत होकर धरतीपर
- **Translation**: 

---

### Verse 10 (Mahabharat 0.435)
- **Original**: सामने ही भगवान्‌ सूर्यसे मिलनेके लिये चल पड़े। सूर्यके उठिये, उठिये। आप-जैसे सत्युरुवको अचेत होकर धरतीपर
- **Translation**: 

---

### Verse 11 (Mahabharat 0.436)
- **Original**: सामने जाकर उन्होंने अपना परिचय दिया और उनके नहीं छोटना चाहियें।' अमृतघोली बोली सुनकर संवरण उठ
- **Translation**: 

---

### Verse 12 (Mahabharat 0.436)
- **Original**: सामने जाकर उन्होंने अपना परिचय दिया और उनके नहीं छोटना चाहियें।' अमृतघोली बोली सुनकर संवरण उठ
- **Translation**: 

---

### Verse 13 (Mahabharat 0.437)
- **Original**: स्वागत-प्रश्न॒ आदिके अनन्तर इच्छाः पूर्ण करनेकी बात गये। उन्होंने कहा, 'सुत्दरि ! मेरे प्राण तुम्हारे हाथ हैं। मैं
- **Translation**: 

---

### Verse 14 (Mahabharat 0.437)
- **Original**: स्वागत-प्रश्न॒ आदिके अनन्तर इच्छाः पूर्ण करनेकी बात गये। उन्होंने कहा, 'सुत्दरि ! मेरे प्राण तुम्हारे हाथ हैं। मैं
- **Translation**: 

---

### Verse 15 (Mahabharat 0.438)
- **Original**: कहनेपर महर्षि बसिश्ठने प्रणामपूर्वक कहा, 'भगवन्‌ ! मैं तुम्हारें बिता जी नहीं सकता। तुम पुझपर दया करें और मुझ
- **Translation**: 

---

### Verse 16 (Mahabharat 0.438)
- **Original**: कहनेपर महर्षि बसिश्ठने प्रणामपूर्वक कहा, 'भगवन्‌ ! मैं तुम्हारें बिता जी नहीं सकता। तुम पुझपर दया करें और मुझ
- **Translation**: 

---

### Verse 17 (Mahabharat 0.439)
- **Original**: राजा संवरणके लिये आपकी कन्या तपतीकी याचना कर्ता सेककको मत छोड़ो । तुम गाश्धर्वविवाहके द्वारा मुझे स्वीकार
- **Translation**: 

---

### Verse 18 (Mahabharat 0.439)
- **Original**: राजा संवरणके लिये आपकी कन्या तपतीकी याचना कर्ता सेककको मत छोड़ो । तुम गाश्धर्वविवाहके द्वारा मुझे स्वीकार
- **Translation**: 

---

### Verse 19 (Mahabharat 0.440)
- **Original**: हूँ। आप उनके उस््बल यश्ञ, धार्मिकता और नीतिज़तासे कर हो। मुझे जीवनदान दो ।' तपतीने कहा; 'राजन्‌ ! मेरे
- **Translation**: 

---

### Verse 20 (Mahabharat 0.440)
- **Original**: हूँ। आप उनके उस््बल यश्ञ, धार्मिकता और नीतिज़तासे कर हो। मुझे जीवनदान दो ।' तपतीने कहा; 'राजन्‌ ! मेरे
- **Translation**: 

---

