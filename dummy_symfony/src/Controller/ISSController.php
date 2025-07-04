<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\JsonResponse;
use Symfony\Component\Routing\Annotation\Route;
use App\Service\ISSService;

class ISSController extends AbstractController
{
    #[Route('/iss', name: 'iss_position', methods: ['GET'])]
    public function iss(ISSService $issService): JsonResponse
    {
        try {
            $data = $issService->getIssPositionWithLocation();
            return $this->json($data);
        } catch (\Exception $e) {
            return $this->json(['error' => 'Failed to fetch ISS position'], 502);
        }
    }
} 